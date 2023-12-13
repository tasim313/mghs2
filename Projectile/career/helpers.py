from uuid import uuid4
import logging

logger = logging.getLogger(__name__)


def get_career_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from .models import Career
    try:
        instance = Career.objects.get(uid=uid)
        career = instance.id
        return career
    except MultipleObjectsReturned:
        instance = Career.objects.filter(uid=uid)[0]
        career = instance.id
        return career
    except ObjectDoesNotExist:
        logging.error("Career does not exist")
    isinstance = Career.objects.filter(uid=uid)
    return isinstance.id


def get_case_study_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from core.models import CaseStudy
    try:
        instance = CaseStudy.objects.get(uid=uid)
        case_study = instance.id
        return case_study
    except MultipleObjectsReturned:
        instance = CaseStudy.objects.filter(uid=uid)[0]
        case_study = instance.id
        return case_study
    except ObjectDoesNotExist:
        logging.error("Case Study does not exist")
    isinstance = CaseStudy.objects.filter(uid=uid)
    return isinstance.id




def get_news_events_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from core.models import NewsEvents
    try:
        instance = NewsEvents.objects.get(uid=uid)
        news_events = instance.id
        return news_events
    except MultipleObjectsReturned:
        instance = NewsEvents.objects.filter(uid=uid)[0]
        news_events = instance.id
        return news_events
    except ObjectDoesNotExist:
        logging.error("News or Events does not exist")
    isinstance = NewsEvents.objects.filter(uid=uid)
    return isinstance.id


def get_news_events_title(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from core.models import NewsEvents
    try:
        instance = NewsEvents.objects.get(uid=uid)
        news_events = instance.headline
        return news_events
    except MultipleObjectsReturned:
        instance = NewsEvents.objects.filter(uid=uid)[0]
        news_events = instance.headline
        return news_events
    except ObjectDoesNotExist:
        logging.error("News or Events does not exist")
    isinstance = NewsEvents.objects.filter(uid=uid)
    return isinstance.headline


def get_news_events_description(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from core.models import NewsEvents
    try:
        instance = NewsEvents.objects.get(uid=uid)
        news_events = instance.description
        return news_events
    except MultipleObjectsReturned:
        instance = NewsEvents.objects.filter(uid=uid)[0]
        news_events = instance.description
        return news_events
    except ObjectDoesNotExist:
        logging.error("News or Events does not exist")
    isinstance = NewsEvents.objects.filter(uid=uid)
    return isinstance.description


def get_news_events_image(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from core.models import NewsEvents
    try:
        instance = NewsEvents.objects.get(uid=uid)
        news_events = instance.image
        return news_events
    except MultipleObjectsReturned:
        instance = NewsEvents.objects.filter(uid=uid)[0]
        news_events = instance.image
        return news_events
    except ObjectDoesNotExist:
        logging.error("News or Events does not exist")
    isinstance = NewsEvents.objects.filter(uid=uid)
    return isinstance.image



def get_case_study_title_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from core.models import CaseStudy
    try:
        instance = CaseStudy.objects.get(uid=uid)
        case_study = instance.title
        return case_study
    except MultipleObjectsReturned:
        instance = CaseStudy.objects.filter(uid=uid)[0]
        case_study = instance.title
        return case_study
    except ObjectDoesNotExist:
        logging.error("CaseStudy does not exist")
    isinstance = CaseStudy.objects.filter(uid=uid)
    return isinstance.title