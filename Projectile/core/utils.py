from uuid import uuid4
import logging

logger = logging.getLogger(__name__)


def get_appointment_slug(instance):
    return (f"{instance.name}{str(instance.uid).split('-')[0]}")

def get_contact_slug(instance):
    return (f"{'webns'}{str(instance.uid).split('-')[0]}")


def get_news_events_slug(instance):
    return (f"{'news and events'}{str(instance.uid).split('-')[0]}")


def get_news_events_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{instance.news_events.uid}{'image'}{instance.news_events.slug}{uid}-{filename}"


def get_news_events_base_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{instance.uid}{'image'}{instance.slug}{uid}-{filename}"


def get_website_logo_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'image'}{'website-logo'}{uid}-{filename}"


def get_home_slider_content_slug(instance):
    return (f"{instance.title}{str(instance.uid).split('-')[0]}")

def get_home_slider_content_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{instance.home_content.title}{'image'}{instance.home_content.slug}{uid}-{filename}"


def get_product_slug(instance):
    return f"{instance.title}"

def get_product_details_slug(instance):
    return f"{instance.products_info.title}{str(instance.uid).split('-')[0]}"


def get_product_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{instance.title}{'image'}{instance.slug}{uid}-{filename}"


def get_product_details_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{instance.title}{'image'}{'details'}{uid}-{filename}"



def get_client_slug(instance):
    return f"{'client'}{str(instance.uid).split('-')[0]}"


def get_client_logo(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{'WEBNS'}{'logo'}{instance.slug}{uid}-{filename}"


def get_testimonial_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{'WEBNS'}{'image'}{uid}-{filename}"



def get_service_slug(instance):
    return f"{instance.title}{str(instance.uid).split('-')[0]}"

def get_service_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{instance.title}{'image'}{instance.slug}{uid}-{filename}"


def get_service_details_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{instance.title}{'image'}{'details'}{uid}-{filename}"


def get_about_file_slug(instance):
    return f"{'about'}{str(instance.uid).split('-')[0]}"

def get_about_file_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{'about'}{'image'}{instance.slug}{uid}-{filename}"


def get_why_choose_us_content_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{'content'}{'image'}{uid}-{filename}"


def get_case_study_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{instance.title}{'image'}{uid}-{filename}"



def get_team_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{instance.name}{'image'}{uid}-{filename}"


def get_gallery_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{'gallery'}{'image'}{uid}-{filename}"


def get_faq_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{instance.title}{'image'}{uid}-{filename}"