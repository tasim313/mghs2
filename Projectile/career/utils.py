from uuid import uuid4

def get_case_study_details_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{instance.title}{'image'}{uid}-{filename}"


def get_news_events_details_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{instance.headline}{'image'}{instance.new_events.slug}{uid}-{filename}"



def get_curriculum_vitae_file(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{'Candidate'}{'cv'}{instance.job_category.designation}{uid}-{filename}"