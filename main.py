#  https://blog.logrocket.com/building-a-graphql-server-with-fastapi/

# заменили starlette.graphql на strawberry.fastapi


from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter

# Определяем типы с помощью strawberry
@strawberry.type
class Course:
    title: str
    description: str
    teacher: str

@strawberry.type
class Query:
    @strawberry.field
    async def courses(self) -> list[Course]:
        return [
            Course(
                title="Python",
                description="Курс по Python",
                teacher="Иван"
            ),
            Course(
                title="GraphQL",
                description="Курс по GraphQL",
                teacher="Мария"
            )
        ]

    @strawberry.field
    async def course(self, title: str) -> Course | None:
        courses = await self.courses()
        return next((c for c in courses if c.title == title), None)

schema = strawberry.Schema(query=Query)

app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)

