from uuid import uuid4
import logging

logger = logging.getLogger(__name__)



def get_news_events_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from .models import NewsEvents
    try:
        instance = NewsEvents.objects.get(uid=uid)
        news_events = instance.id
        return news_events
    except MultipleObjectsReturned:
        instance = NewsEvents.objects.filter(uid=uid)[0]
        news_events = instance.id
        return news_events
    except ObjectDoesNotExist:
        logging.error("News_events does not exist")
    isinstance = NewsEvents.objects.filter(uid=uid)
    return isinstance.id


def get_home_slider_content_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from .models import HomeSliderContent
    try:
        instance = HomeSliderContent.objects.get(uid=uid)
        slider_content = instance.id
        return slider_content
    except MultipleObjectsReturned:
        instance = HomeSliderContent.objects.filter(uid=uid)[0]
        slider_content = instance.id
        return slider_content
    except ObjectDoesNotExist:
        logging.error("News_events does not exist")
    isinstance = HomeSliderContent.objects.filter(uid=uid)
    return isinstance.id


def get_about_file_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from .models import About
    try:
        instance = About.objects.get(uid=uid)
        about_file = instance.id
        return about_file
    except MultipleObjectsReturned:
        instance = About.objects.filter(uid=uid)[0]
        about_file = instance.id
        return about_file
    except ObjectDoesNotExist:
        logging.error("AboutFile does not exist")
    isinstance = About.objects.filter(uid=uid)
    return isinstance.id


def get_why_choose_content_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from .models import WhyChooseUs
    try:
        instance = WhyChooseUs.objects.get(uid=uid)
        content = instance.id
        return content
    except MultipleObjectsReturned:
        instance = WhyChooseUs.objects.filter(uid=uid)[0]
        content = instance.id
        return content
    except ObjectDoesNotExist:
        logging.error("content does not exist")
    isinstance = WhyChooseUs.objects.filter(uid=uid)
    return isinstance.id



def get_product_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from .models import Product
    try:
        instance = Product.objects.get(uid=uid)
        product = instance.id
        return product
    except MultipleObjectsReturned:
        instance = Product.objects.filter(uid=uid)[0]
        product = instance.id
        return product
    except ObjectDoesNotExist:
        logging.error("Product does not exist")
    isinstance = Product.objects.filter(uid=uid)
    return isinstance.id



def get_service_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from .models import Service
    try:
        instance = Service.objects.get(uid=uid)
        service = instance.id
        return service
    except MultipleObjectsReturned:
        instance = Service.objects.filter(uid=uid)[0]
        service = instance.id
        return service
    except ObjectDoesNotExist:
        logging.error("Service does not exist")
    isinstance = Service.objects.filter(uid=uid)
    return isinstance.id


def get_FrequentAskedQuestion_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from .models import FrequentAskedQuestion
    try:
        instance = FrequentAskedQuestion.objects.get(uid=uid)
        faq = instance.id
        return faq
    except MultipleObjectsReturned:
        instance = FrequentAskedQuestion.objects.filter(uid=uid)[0]
        faq = instance.id
        return FrequentAskedQuestion
    except ObjectDoesNotExist:
        logging.error("FrequentAskedQuestion does not exist")
    isinstance = FrequentAskedQuestion.objects.filter(uid=uid)
    return isinstance.id



def get_product_title_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from .models import Product
    try:
        instance = Product.objects.get(uid=uid)
        product = instance.title
        return product
    except MultipleObjectsReturned:
        instance = Product.objects.filter(uid=uid)[0]
        product = instance.title
        return product
    except ObjectDoesNotExist:
        logging.error("Product does not exist")
    isinstance = Product.objects.filter(uid=uid)
    return isinstance.title


def get_product_short_description_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from .models import Product
    try:
        instance = Product.objects.get(uid=uid)
        product = instance.short_description
        return product
    except MultipleObjectsReturned:
        instance = Product.objects.filter(uid=uid)[0]
        product = instance.short_description
        return product
    except ObjectDoesNotExist:
        logging.error("Product does not exist")
    isinstance = Product.objects.filter(uid=uid)
    return isinstance.short_description



def get_product_image_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from .models import Product
    try:
        instance = Product.objects.get(uid=uid)
        product = instance.image
        return product
    except MultipleObjectsReturned:
        instance = Product.objects.filter(uid=uid)[0]
        product = instance.image
        return product
    except ObjectDoesNotExist:
        logging.error("Product does not exist")
    isinstance = Product.objects.filter(uid=uid)
    return isinstance.image




def get_service_title_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from .models import Service
    try:
        instance = Service.objects.get(uid=uid)
        service = instance.title
        return service
    except MultipleObjectsReturned:
        instance = Service.objects.filter(uid=uid)[0]
        service = instance.title
        return service
    except ObjectDoesNotExist:
        logging.error("Service does not exist")
    isinstance = Service.objects.filter(uid=uid)
    return isinstance.title


def get_service_short_description_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from .models import Service
    try:
        instance = Service.objects.get(uid=uid)
        service = instance.short_description
        return service
    except MultipleObjectsReturned:
        instance = Service.objects.filter(uid=uid)[0]
        service = instance.short_description
        return service
    except ObjectDoesNotExist:
        logging.error("Service does not exist")
    isinstance = Service.objects.filter(uid=uid)
    return isinstance.short_description



def get_service_image_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from .models import Service
    try:
        instance = Service.objects.get(uid=uid)
        service = instance.image
        return service
    except MultipleObjectsReturned:
        instance = Service.objects.filter(uid=uid)[0]
        service = instance.image
        return service
    except ObjectDoesNotExist:
        logging.error("Service does not exist")
    isinstance = Service.objects.filter(uid=uid)
    return isinstance.image