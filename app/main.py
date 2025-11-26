from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(..., description="Service health status")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Current UTC timestamp")


class ClassroomQuery(BaseModel):
    question: str = Field(..., description="Student question or discussion prompt")
    course: Optional[str] = Field(None, description="Course name or topic for context")


class ClassroomInsight(BaseModel):
    summary: str
    follow_up_questions: List[str]
    interactive_ideas: List[str]


class ResearchPrompt(BaseModel):
    title: str = Field(..., description="Paper title")
    abstract: str = Field(..., description="Paper abstract or summary")


class ResearchSummary(BaseModel):
    overview: str
    key_terms: List[str]
    next_steps: List[str]


class CampusServiceRequest(BaseModel):
    intent: str = Field(..., description="Service request type, e.g. navigation, schedule, support")
    detail: Optional[str] = Field(None, description="Extra context provided by the user")


class CampusServicePlan(BaseModel):
    intent: str
    actions: List[str]
    resources: List[str]


app = FastAPI(title="Campus Assistant Backend", version="0.1.0")


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Simple health check endpoint."""
    return HealthResponse(status="ok")


@app.post("/classroom/ask", response_model=ClassroomInsight)
def classroom_assistant(payload: ClassroomQuery) -> ClassroomInsight:
    """Provide lightweight reasoning scaffolds for classroom Q&A or discussions."""
    base_context = payload.course or "课堂"
    follow_up = [
        f"在{base_context}中，提出一个需要举例说明的问题。",
        "请同学们用自己的语言解释这个概念。",
        "把问题与实际案例联系起来。",
    ]
    interactive = [
        "快速投票收集观点",
        "分组讨论并分享结论",
        "即兴演示或白板演练",
    ]
    summary = f"已收到问题：{payload.question}。为{base_context}生成讨论思路。"
    return ClassroomInsight(summary=summary, follow_up_questions=follow_up, interactive_ideas=interactive)


@app.post("/research/summarize", response_model=ResearchSummary)
def research_summarize(prompt: ResearchPrompt) -> ResearchSummary:
    """Create a structured digest for academic papers."""
    overview = (
        f"《{prompt.title}》摘要显示研究聚焦于核心议题，" "提供了关键方法与实验结果的初步洞察。"
    )
    key_terms = ["数据集", "方法论", "实验指标"]
    next_steps = [
        "生成批判性问题，检查实验假设和限制。",
        "提取可重复实验的配置与参数。",
        "为阅读小组准备三条讨论要点。",
    ]
    return ResearchSummary(overview=overview, key_terms=key_terms, next_steps=next_steps)


@app.post("/campus/service", response_model=CampusServicePlan)
def campus_service(payload: CampusServiceRequest) -> CampusServicePlan:
    """Draft an action plan for common campus service intents."""
    actions = [
        f"确认用户意图：{payload.intent}",
        "调取校园地图、课表或通知等数据源",
        "生成操作清单并推送到移动端提醒",
    ]
    resources = ["校园地图", "课程表API", "办事指南"]
    return CampusServicePlan(intent=payload.intent, actions=actions, resources=resources)
