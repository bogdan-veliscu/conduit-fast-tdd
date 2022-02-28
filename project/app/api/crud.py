from typing import Optional, List
from app.models.pydantic import SummmaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummmaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="dummy summary")

    await summary.save()
    return summary.id


async def get(id: int) -> Optional[dict]:
    summary = await TextSummary.filter(id=id).first().values()

    if summary:
        return summary
    return None


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries
