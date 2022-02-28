from pydantic import BaseModel


class SummmaryPayloadSchema(BaseModel):
    url: str


class SummaryResponseSchema(SummmaryPayloadSchema):
    id: int
