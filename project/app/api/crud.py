from app.models.pydantic import SummmaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummmaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="dummy summary")

    await summary.save()
    return summary.id
