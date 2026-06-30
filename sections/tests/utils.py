from users.models import User, UserRoles
from sections.models import Section, Content, Question



def get_admin_user():
    user = User.objects.create(
        email="example45@example.com",
        role=UserRoles.ADMIN,
        is_staff=True,
        is_superuser=True,
        is_active=True,
    )

    user.set_password('12346789')
    user.save()
    return user

def get_member_user():
    user = User.objects.create(
        email="member45@example.com",
        role=UserRoles.MEMBER,
        is_staff=False,
        is_superuser=False,
        is_active=True,
    )

    user.set_password('12346789')
    user.save()
    return user



def get_test_section():
    section = Section.objects.create(
        title="Test Section",
        description="This is a test section",

    )

    return section



def get_test_content():
    section = get_test_section()
    content = Content.objects.create(
        section=section,
        title="Test Title Content",
        content="This is a test content",

    )
    return content


def get_test_question():
    content = get_test_content()
    question = Question.objects.create(
        section=content.section,
        description="This is a test question description",
        question = "This is a test question",
        answer = content,

    )
    return question
