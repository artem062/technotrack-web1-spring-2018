from categories.models import Category
from questions.models import Question
from stackoverflow import cache


def stats(request):
    tot_cat = cache.get('total_categories')
    if tot_cat is None:
        tot_cat = Category.objects.count()
        cache.set('total_categories', tot_cat, 30)
    tot_quest = cache.get('total_questions')
    if tot_quest is None:
        tot_quest = Question.objects.count()
        cache.set('total_questions', tot_quest, 30)
    return {
        'total_categories': tot_cat,
        'total_questions': tot_quest,
        }

