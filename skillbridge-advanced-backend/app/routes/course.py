from fastapi import APIRouter

router = APIRouter()

@router.get("/recommend")
def recommend_courses(score: int):
    if score < 7:
        level = "Beginner"
        courses = ["Digital Basics", "Typing", "Internet Use"]
    elif score < 14:
        level = "Intermediate"
        courses = ["MS Office", "Online Job Search", "Intro to Web"]
    else:
        level = "Advanced"
        courses = ["Python", "Freelancing", "Blockchain"]
    return {"level": level, "courses": courses}
