# from django.db import models

# # Create your models here.

# # class SourceMode(models.Model):
# #     Name = models.CharField(unique=True, max_length=50, null=False)

# #     def __str__(self):
# #         return self.Name

# # class Status(models.Model):
# #     Status = models.CharField(unique=True, max_length=50, null=False)

# #     def __str__(self):
# #         return self.Status

# # class CandidateData(models.Model):
# #     Candidate_Name = models.CharField(max_length=75, null=True)
# #     Candidate_Email = models.EmailField(unique=True, null=True)
# #     Candidate_Resumescore = models.PositiveIntegerField(null=True)
# #     Candidate_Jobrole = models.CharField(max_length=75, null=True)
# #     Candidate_Yearsofexperience = models.PositiveIntegerField(null=True)
# #     Candidate_Contact = models.CharField(max_length = 100,unique=True, null=True)
# #     Candidate_Yearofgraduation = models.CharField(max_length=75,null=True)

# #     Candidate_Location = models.CharField(null=True, max_length=100)
# #     Candidate_Qualification = models.CharField(max_length=100, null=True)
# #     Candidate_DomainExp = models.IntegerField(null=True)
# #     Candidate_PreExperience = models.IntegerField(null=True)
# #     Candidate_Reason = models.CharField(null=True, max_length=50)
# #     Candidate_TravelConstraint = models.CharField(null=True, max_length=100)
# #     Candidate_Sourcemode = models.ForeignKey(SourceMode, on_delete=models.CASCADE, null=True)
# #     Candidate_RefName = models.CharField(max_length=50)
# #     Candidate_RefEmail = models.EmailField(unique = True, null=True)
# #     Candidate_NotificationPeriod = models.CharField(null=True, max_length=50)
# #     Candidate_Fatheroccupation = models.CharField(null=True, max_length=50)
# #     Candidate_Motheroccupation = models.CharField(null=True, max_length=50)
# #     Candidate_Siblings = models.CharField(null=True, max_length=50)
# #     Candidate_status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
# #     Remarks = models.CharField(max_length=500)
# class llmCandidateData(models.Model):
#     resume = models.FileField()
#     resumeId = models.IntegerField(unique=True, null=True)
#     name = models.CharField(max_length=75, null=True)
#     email = models.EmailField(unique=True, null=True)
#     resumeScore = models.PositiveIntegerField( null=True)
#     jobRole = models.CharField(max_length=75, null=True)
#     yearsOfExperience = models.PositiveIntegerField(null=True)
#     phoneNo = models.CharField(max_length = 100,unique=True, null=True)
#     yearOfGraduation = models.CharField(max_length=75,null=True)    
    
    
#     location = models.CharField(null=True, max_length=100)
#     qualification = models.CharField(max_length=100, null=True)
#     domainExperience = models.IntegerField(null=True)
#     reason = models.CharField(null=True, max_length=50)
#     travelConstraint = models.CharField(null=True, max_length=100)
#     sourceMode = models.ForeignKey(SourceMode, on_delete=models.CASCADE, null=True)
#     referenceName = models.CharField(max_length=50)
#     referenceEmail = models.EmailField(unique = True, null=True)
#     notificationPeriod = models.CharField(null=True, max_length=50)
#     fatherOccupation = models.CharField(null=True, max_length=50)
#     motherOccupation = models.CharField(null=True, max_length=50)
#     siblings = models.CharField(null=True, max_length=50)
#     status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
#     remarks = models.CharField(max_length=500)

#     #JSON DATA RECEIVED :
#     # {'Name': 'Jane Smith', 'Email': 'janesmith@email.com', 'Resume_score': 69, 'Job_Role': 'Sales', 'Experience': 8, 'phone': '555-987-6543', 'Year_of_Graduation': 'N/A'}


#     def __str__(self):
#         return self.name