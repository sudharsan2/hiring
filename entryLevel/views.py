# from django.shortcuts import render

# # Create your views here.
# def sorting_applicants_on_resume_score(request):    
#     sorted_objects = applicants.objects.all().order_by('resume_score')
#     serializer = applicants_serializer(sorted_objects, many= True)
#     return serializer.data
 
# class assign_resume(APIView):
#     def post(self,request):
#         n= int(request.data.get('num',None))
#         roles = request.data.get('role',None)
#         users = CustomUser.objects.all()
#         users_id = [hr.employee_id for hr in users if (hr.role == "HR" and hr.leave == False)]
#         count =0
#         sorted_resumes = sorting_applicants_on_resume_score()
#         for key,values in sorted_resumes.items():
#             if values['assigned_to']==None and values['job_role']== roles:
#                 existing_resume = applicants.objects.get(id = values['id'])
#                 values['assigned_to']= users_id[count]
#                 existing_resume.assigned_to =users_id[count]
#                 existing_resume.save()
#                 if count<len(users_id):
#                     count+=1
#                 else:
#                     count=0
 
# class get_assigned_resume(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self,request):
#         user = request.user
#         if user.role == "hr":
#             resumes= applicants.objects.get(assigned_to = user.name)
#             serializer = applicants_serializer(resumes, many =True)
#             serialized_data = serializer.data
#             return Response(serialized_data)