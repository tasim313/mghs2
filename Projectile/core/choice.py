from django.db import models


class UserRole(models.TextChoices):
    Admin = 'Admin', 'admin'
    Manager = 'Manager', 'manager'
    hr = 'Human resources (HR)', 'human resources (hr)'
    accounts = 'Accounts', 'accounts'


class UserStatus(models.TextChoices):
    Active = 'Active', 'active'
    Inactive = 'Inactive', 'inactive'
    Delete = 'Delete', 'delete'


class ProvidedService(models.TextChoices):
    SoftwareDevelopment = 'Software Development', 'software development'
    Manufacturing_Sales_Industry = 'Automated Business Solution for Manufacturing & Sales Industry', 'automated business solution for manufacturing & sales industry'
    ERP = 'StepsERP, The Ultimate ERP for Manufacture Based Industry', 'stepsERP, the ultimate ERP for manufacture based Industry'
    HRM = 'Human Resource Management and Accounting & Financial System for Hospitals & Diagnostics', 'Human Resource Management and Accounting &Financial System for Hospitals & Diagnostics'
    Application = 'Application Development (Client Server)', 'application development (Client Server)'
    Web = 'Web & Web Application Development', 'Web & Web Application Development'
    Document_Management = 'Online Document Management System', 'Online Document Management System'
    Mobile_Application = 'Android and iOS based Mobile Application Development', 'Android and iOS based Mobile Application Development'
    Network_design = 'Network Design, Administering & Consulting', 'Network Design, Administering & Consulting'
    ICT_Consulting = 'Total ICT Setup & Consultancy', 'Total ICT Setup & Consultancy'


class NewsEventsStatus(models.TextChoices):
    news = 'News', 'news'
    events = 'Events', 'events'