We are excited you are taking the time to solve our technical assignment! | ![craftable software](https://drive.google.com/uc?id=1ZIRznbixr8JX8qRJcVbOj6GVMtPgeGhG "craftable software")
------------- | -------------


Let’s pretend you are starting your first day with us. After you settle in, your first task will be assigned. Both Joseph (Product Owner) and Ness (Technical Lead) are ready to give you more details on your first task.

> Joseph - “Hi, I have your first task, excited?

> As you know, we have a website that sells multiple types of products, but more importantly we sell the vast majority of our products to customers in three countries United Kingdom, Portugal and United States. We have been having reports lately that the prices don't add up when you take into consideration the exchange rates, this has caused multiple issues in our finance department."

> Ness - “Ok, I understand the problem and I think I can provide some help, our exchange rate calculator has been problematic, some to our fault some to our third party provider. We need to create a test suite that allows us to improve the quality and coverage of our website. We have a staging environment at [http://tutorialsninja.com/demo](http://tutorialsninja.com/demo) and we should use it to run some automation tests. 
> I believe we need to pick three tests to start with and the focus should be on what is critical for the website to run, would you be able to help us? Pro-tip, have a look at our third party provider documentation, [https://free.currencyconverterapi.com/](https://free.currencyconverterapi.com/) it might give you some testing ideas."

### To start you need to be aware of some premises for this challenge ###:

* You need to use singer.io, an open source tool, to create pipelines. You can download it here: https://www.singer.io
* The CSV with the customer data is available here.
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