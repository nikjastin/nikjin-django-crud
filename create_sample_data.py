#!/usr/bin/env python
"""
Script to create sample data for the NikJin CRUD application
Run this after setting up the database: python create_sample_data.py
"""

import os
import sys
import django
from datetime import datetime, timedelta
from django.utils import timezone

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nikjin_project.settings')
django.setup()

from django.contrib.auth.models import User
from main_app.models import UserProfile, Task, Project

def create_sample_data():
    print("Creating sample data...")
    
    # Create sample users
    users_data = [
        {'username': 'john_doe', 'email': 'john@example.com', 'first_name': 'John', 'last_name': 'Doe'},
        {'username': 'jane_smith', 'email': 'jane@example.com', 'first_name': 'Jane', 'last_name': 'Smith'},
        {'username': 'mike_wilson', 'email': 'mike@example.com', 'first_name': 'Mike', 'last_name': 'Wilson'},
        {'username': 'sarah_jones', 'email': 'sarah@example.com', 'first_name': 'Sarah', 'last_name': 'Jones'},
        {'username': 'david_brown', 'email': 'david@example.com', 'first_name': 'David', 'last_name': 'Brown'},
    ]
    
    created_users = []
    for user_data in users_data:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'email': user_data['email'],
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name'],
            }
        )
        if created:
            user.set_password('password123')
            user.save()
            print(f"Created user: {user.username}")
        created_users.append(user)
    
    # Create sample projects
    projects_data = [
        {
            'name': 'E-commerce Website',
            'description': 'Building a modern e-commerce platform with Django and React',
            'manager': created_users[0],
            'members': [created_users[0], created_users[1], created_users[2]],
            'deadline': timezone.now() + timedelta(days=60),
        },
        {
            'name': 'Mobile App Development',
            'description': 'Creating a cross-platform mobile application using React Native',
            'manager': created_users[1],
            'members': [created_users[1], created_users[3], created_users[4]],
            'deadline': timezone.now() + timedelta(days=45),
        },
        {
            'name': 'Data Analytics Dashboard',
            'description': 'Developing a comprehensive analytics dashboard for business intelligence',
            'manager': created_users[2],
            'members': [created_users[2], created_users[0], created_users[4]],
            'deadline': timezone.now() + timedelta(days=30),
        },
    ]
    
    created_projects = []
    for project_data in projects_data:
        project, created = Project.objects.get_or_create(
            name=project_data['name'],
            defaults={
                'description': project_data['description'],
                'manager': project_data['manager'],
                'deadline': project_data['deadline'],
            }
        )
        if created:
            project.members.set(project_data['members'])
            print(f"Created project: {project.name}")
        created_projects.append(project)
    
    # Create sample tasks
    tasks_data = [
        {
            'title': 'Setup Django Backend',
            'description': 'Initialize Django project with proper structure and basic models',
            'priority': 'high',
            'status': 'completed',
            'assigned_to': created_users[0],
            'created_by': created_users[1],
            'due_date': timezone.now() + timedelta(days=7),
        },
        {
            'title': 'Design User Interface',
            'description': 'Create wireframes and mockups for the main user interface',
            'priority': 'high',
            'status': 'in_progress',
            'assigned_to': created_users[1],
            'created_by': created_users[0],
            'due_date': timezone.now() + timedelta(days=10),
        },
        {
            'title': 'Implement Authentication',
            'description': 'Add user registration, login, and password reset functionality',
            'priority': 'high',
            'status': 'pending',
            'assigned_to': created_users[2],
            'created_by': created_users[0],
            'due_date': timezone.now() + timedelta(days=14),
        },
        {
            'title': 'Database Optimization',
            'description': 'Optimize database queries and add proper indexing',
            'priority': 'medium',
            'status': 'pending',
            'assigned_to': created_users[3],
            'created_by': created_users[2],
            'due_date': timezone.now() + timedelta(days=21),
        },
        {
            'title': 'API Documentation',
            'description': 'Create comprehensive API documentation using Swagger',
            'priority': 'medium',
            'status': 'pending',
            'assigned_to': created_users[4],
            'created_by': created_users[1],
            'due_date': timezone.now() + timedelta(days=28),
        },
        {
            'title': 'Unit Testing',
            'description': 'Write comprehensive unit tests for all major components',
            'priority': 'high',
            'status': 'in_progress',
            'assigned_to': created_users[0],
            'created_by': created_users[2],
            'due_date': timezone.now() + timedelta(days=35),
        },
        {
            'title': 'Performance Testing',
            'description': 'Conduct load testing and performance optimization',
            'priority': 'medium',
            'status': 'pending',
            'assigned_to': created_users[1],
            'created_by': created_users[3],
            'due_date': timezone.now() + timedelta(days=42),
        },
        {
            'title': 'Security Audit',
            'description': 'Perform security audit and implement necessary fixes',
            'priority': 'high',
            'status': 'pending',
            'assigned_to': created_users[2],
            'created_by': created_users[4],
            'due_date': timezone.now() + timedelta(days=49),
        },
        {
            'title': 'Deployment Setup',
            'description': 'Configure production deployment with CI/CD pipeline',
            'priority': 'medium',
            'status': 'pending',
            'assigned_to': created_users[3],
            'created_by': created_users[0],
            'due_date': timezone.now() + timedelta(days=56),
        },
        {
            'title': 'User Training',
            'description': 'Create user manuals and conduct training sessions',
            'priority': 'low',
            'status': 'pending',
            'assigned_to': created_users[4],
            'created_by': created_users[1],
            'due_date': timezone.now() + timedelta(days=63),
        },
    ]
    
    for task_data in tasks_data:
        task, created = Task.objects.get_or_create(
            title=task_data['title'],
            defaults=task_data
        )
        if created:
            print(f"Created task: {task.title}")
    
    print("\nSample data creation completed!")
    print(f"Created {User.objects.count()} users")
    print(f"Created {Project.objects.count()} projects")
    print(f"Created {Task.objects.count()} tasks")
    print("\nYou can now login with any of these users:")
    for user in created_users:
        print(f"  Username: {user.username}, Password: password123")

if __name__ == '__main__':
    create_sample_data()
