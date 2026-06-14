path('submit/', views.submit, name='submit')
path('course/<int:course_id>/submit/', views.submit, name='submit')
path('show_exam_result/<int:submission_id>/', views.show_exam_result, name='show_exam_result')
