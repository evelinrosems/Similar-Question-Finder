from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.schemas.question import QuestionCreate, QuestionResponse, QuestionSearchResponse
from app.schemas.user import UserResponse
from app.models.user import User
from app.models.question import Question
from app.core.ml import ml_service
from app.api.endpoints.auth import get_current_user
from app.db.database import get_db

router = APIRouter()

@router.post("/", response_model=QuestionResponse)
async def submit_question(
    question_in: QuestionCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Generate embedding
    embedding = ml_service.get_embedding(question_in.text)

    # Assign topic from text (NOT embedding)
    topic = ml_service.assign_topic(question_in.text)

    new_question = Question(
        user_id=current_user.id,
        text=question_in.text,
        embedding=embedding,
        topic=topic
    )

    db.add(new_question)
    await db.commit()
    await db.refresh(new_question)

    return new_question

@router.get("/history", response_model=list[QuestionResponse])
async def get_history(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Question)
        .where(Question.user_id == current_user.id)
        .order_by(Question.created_at.desc())
    )
    questions = result.scalars().all()
    
    return questions

@router.post("/search", response_model=list[QuestionSearchResponse])
async def search_questions(
    question_in: QuestionCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    try:
        # Generate query embedding
        query_embedding = ml_service.get_embedding(question_in.text)

        # Fetch all questions
        result = await db.execute(select(Question))
        all_questions = result.scalars().all()

        results = []

        for q in all_questions:
            if q.embedding:

                try:
                    score = ml_service.compute_cosine_similarity(
                        query_embedding,
                        q.embedding
                    )
                except Exception as e:
                    print(f"Similarity Error: {e}")
                    score = 0.0

                results.append({
                    "id": q.id,
                    "text": q.text,
                    "topic": q.topic,
                    "score": score
                })

        # Sort by similarity
        results.sort(key=lambda x: x["score"], reverse=True)

        return [
            QuestionSearchResponse(**r)
            for r in results[:5]
        ]

    except Exception as e:
        print(f"Search Endpoint Error: {e}")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
