We are excited you are taking the time to solve our technical assignment! | ![craftable software](https://drive.google.com/uc?id=1ZIRznbixr8JX8qRJcVbOj6GVMtPgeGhG "craftable software")
------------- | -------------



Let’s pretend you are starting your first day with us. After you settle in, your first task will be assigned. Both Joseph (Product Owner) and Ness (Technical Lead) are ready to give you more details on your first task.

> Joseph - “Hi, I have your first task, excited? 

> We need to create an ETL Transformation that allows us to correlate company information with the latitude and longitude coordinates so that our drivers can find the addresses of our customers more easily. We have a .csv file but we need to find the lat long based on the postcode. I also need to know if there are any special characters in the company name and to simplify display the company name without special characters to help our drivers. Finally we need to have the resulting data in a new database so that is accessible to the company that handles the drivers.”

> Ness - “Ok, I understand the request and I think we can provide some help. I’ve heard about https://postcodes.io/, and we can use it as a web service where we can type the postcode and we get the address details back, alongside the latitude and longitude. As for the special characters, we will exclude: ~, `, !, @, #,%,&,* and similar and  I think we can use some tools to identify and then transform the name of the company. For the specific need of having the information publicly available, I believe storing this data in Postgres database would be perfect as we would then be able to expose it to someone specific based on credentials. I would say we should do a proof of concept to confirm this can actually work”.

### To start you need to be aware of some premises for this challenge

* You need to use singer.io, an open source tool, to create pipelines. You can download it here: [singer.io](https://www.singer.io)
* The CSV with the customer data is available *[here](https://docs.google.com/spreadsheets/d/e/2PACX-1vSyWCJtr4zXPapIzqowojAyB7fyyhBMH5YlLBc5E8xP7tjoBGIlLBIHrp6AvN12saGAsRNvCclIcIfd/pub?gid=0&single=true&output=csv)*
* A working example for the web service is: http://api.postcodes.io/postcodes/N76RS
* Postgres docker image: https://hub.docker.com/_/postgres 


A valid example of the expected outcome, delivered in a postgres table iis:

| PostCode      | Name           | Phone     |   Country  |   County  |   Long    | Lat       |HasSpecialCharacters|NoSpecialCharacters |
|:-------------:|:--------------:|:---------:|:----------:|:---------:|:---------:|:---------:|:------------------:|:------------------:|
|  N76RS        |   Friends’r Us | 123456790 |  England   |   London  | -0.116805 |51.560414  |               True | Friendsr Us        |
| SW46TA        |   StayLocal    | 78945613  |  England   |   London  | -0.12278  |51.472716  |              False | StayLocal          |




Once you are done please save all files, docker images and resources in your solution and commit the code and create a Pull Request so we can code review it. (see a more detailed explanation about the commit in the explanation below)”

---

Now that the exercise has been explained, you can start working on it. We normally request for it to be uploaded into our git repository within 5 working days, but can be changed if you need more time to start. This task should take you no longer than 3 hours and needless to say should be totally completed by you, after all this is supposed to be a fun challenge! 
We will provide you a git repository in bitbucket for the code to be uploaded. Please see the instructions below:

* Please sign up for an account on Bitbucket if you don't have one already. If you do, feel free to use your own login / profile. If you're not familiar with GIT, use the Sourcetree client to get started or visit http://git-scm.com for the official git client.
* Once you're done with your work, COMMIT and then PUSH (ie. send to bitbucket). The PUSH will notify us but it is important you let us know you are done. Only push when you're done, and push once. This is to avoid us reviewing an incomplete submission.

### We're here to help...
Should you run into problems or have any questions please get in touch with Renato Oliveira - renato.oliveira@craftablesoftware.com



Good luck from everyone here at craftable!