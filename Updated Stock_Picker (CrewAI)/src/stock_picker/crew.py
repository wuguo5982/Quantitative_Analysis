from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from pydantic import BaseModel, Field
from crewai_tools import SerperDevTool
from .tools.push_tool import send_push_notification


class TrendingCompany(BaseModel):
    """ A company that is in the news and attracting attention """
    name: str = Field(description="Company name")
    ticker: str = Field(description="Stock ticker symbol")
    reason: str = Field(description="Reason this company is trending in the news")

class TrendingCompanyList(BaseModel):
    """ List of multiple trending companies that are in the news """
    companies: list[TrendingCompany] = Field(description="List of companies trending in the news")

class TrendingCompanyResearch(BaseModel):
    """ Detailed research on a company """
    name: str = Field(description="Company name")
    market_position: str = Field(description="Current market position and competitive analysis")
    future_outlook: str = Field(description="Future outlook and growth prospects")
    investment_potential: str = Field(description="Investment potential and suitability for investment")

class TrendingCompanyResearchList(BaseModel):
    """ A list of detailed research on all the companies """
    research_list: list[TrendingCompanyResearch] = Field(description="Comprehensive research on all trending companies")


@CrewBase
class StockPicker():
    """StockPicker crew"""

    agents: list[BaseAgent]
    tasks: list[Task]


    @agent
    def trending_company_finder(self) -> Agent:
        return Agent(config=self.agents_config['trending_company_finder'],
                     tools=[SerperDevTool()], memory=True)
    
    @agent
    def financial_researcher(self) -> Agent:
        return Agent(config=self.agents_config['financial_researcher'],
                     tools=[SerperDevTool()], memory=True)

    @agent
    def stock_picker(self) -> Agent:
        return Agent(config=self.agents_config['stock_picker'], 
                     memory=True)
    
    @task
    def find_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config['find_trending_companies'],
            output_pydantic=TrendingCompanyList,
        )

    @task
    def research_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config['research_trending_companies'],
            output_pydantic=TrendingCompanyResearchList,
        )

    @task
    def pick_best_company(self) -> Task:
        return Task(
            config=self.tasks_config['pick_best_company'],
        )




    @agent
    def fundamental_analyst(self) -> Agent:
        return Agent(config=self.agents_config["fundamental_analyst"], tools=[SerperDevTool()], memory=False, max_iter=5, max_retry_limit=2)

    @agent
    def valuation_analyst(self) -> Agent:
        return Agent(config=self.agents_config["valuation_analyst"], tools=[SerperDevTool()], memory=False, max_iter=5, max_retry_limit=2)

    @agent
    def institutional_flow_analyst(self) -> Agent:
        return Agent(config=self.agents_config["institutional_flow_analyst"], tools=[SerperDevTool()], memory=False, max_iter=5, max_retry_limit=2)

    @agent
    def options_microstructure_analyst(self) -> Agent:
        return Agent(config=self.agents_config["options_microstructure_analyst"], tools=[SerperDevTool()], memory=False, max_iter=5, max_retry_limit=2)

    @agent
    def price_technical_analyst(self) -> Agent:
        return Agent(config=self.agents_config["price_technical_analyst"], tools=[SerperDevTool()], memory=False, max_iter=5, max_retry_limit=2)

    @agent
    def catalyst_news_analyst(self) -> Agent:
        return Agent(config=self.agents_config["catalyst_news_analyst"], tools=[SerperDevTool()], memory=False, max_iter=5, max_retry_limit=2)

    @agent
    def analyst_consensus_analyst(self) -> Agent:
        return Agent(config=self.agents_config["analyst_consensus_analyst"], tools=[SerperDevTool()], memory=False, max_iter=5, max_retry_limit=2)

    @agent
    def evidence_auditor(self) -> Agent:
        return Agent(config=self.agents_config["evidence_auditor"], tools=[SerperDevTool()], memory=False, max_iter=5, max_retry_limit=2)

    @agent
    def ranking_analyst(self) -> Agent:
        return Agent(config=self.agents_config["ranking_analyst"], tools=[SerperDevTool()], memory=False, max_iter=5, max_retry_limit=2)

    @agent
    def final_judge(self) -> Agent:
        return Agent(config=self.agents_config["final_judge"], tools=[SerperDevTool()], memory=False, max_iter=5, max_retry_limit=2)

    @task
    def screen_universe(self) -> Task:
        return Task(config=self.tasks_config["screen_universe"])

    @task
    def analyze_fundamentals(self) -> Task:
        return Task(config=self.tasks_config["analyze_fundamentals"])

    @task
    def analyze_valuation(self) -> Task:
        return Task(config=self.tasks_config["analyze_valuation"])

    @task
    def analyze_institutional(self) -> Task:
        return Task(config=self.tasks_config["analyze_institutional"])

    @task
    def analyze_microstructure(self) -> Task:
        return Task(config=self.tasks_config["analyze_microstructure"])

    @task
    def analyze_technicals(self) -> Task:
        return Task(config=self.tasks_config["analyze_technicals"])

    @task
    def analyze_catalysts(self) -> Task:
        return Task(config=self.tasks_config["analyze_catalysts"])

    @task
    def analyze_consensus(self) -> Task:
        return Task(config=self.tasks_config["analyze_consensus"])

    @task
    def audit_evidence(self) -> Task:
        return Task(config=self.tasks_config["audit_evidence"])

    @task
    def rank_top50(self) -> Task:
        return Task(config=self.tasks_config["rank_top50"])

    @task
    def judge_top5(self) -> Task:
        return Task(config=self.tasks_config["judge_top5"])

    @crew
    def crew(self) -> Crew:
        """Creates the StockPicker crew"""
        
        manager = Agent(
            config=self.agents_config['manager'],
            allow_delegation=True
        )
        

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            verbose=True,
            tracing=False,
            memory=False,
            manager_agent=manager
       
        )
