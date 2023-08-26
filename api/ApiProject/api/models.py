from django.db import models

# Create your models here.
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=1000)
    about= models.TextField()
    type=models.CharField(max_length=100,choices=(('IT', 'IT'),('Non IT', 'Non IT'),('Mobile phones' , 'Mobile phones')))
    active=models.BooleanField(default=False)

    #def __str__(self):
      #  return self.name #it shows the company name  when acessed by any object 
   # def __str__(self):
      #  return self.location ##it overrides the data of showing company name  
                            ## it returns location name instead of company name
    ### instead we can concate this ######

    def __str__(self):
        return self.name +"--" + self.location
    

    ##### To get the employees of any particular company id #####
    ### we have to use new  customized url : companies/companyid/employees  


#Employee Model
class Employee(models.Model):
    name= models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50 ,choices=(("Manager" ,'manager'),
                                                      ('Software Developer' ,'Software Developer'),
                                                      ('project Leader' ,'Project Leader')
                                                      ))
    company= models.ForeignKey(Company,on_delete=models.CASCADE)

