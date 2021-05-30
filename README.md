## generate a data 
Suppose that we we have a sales website, we will, in the first part, simulate 2 data inputs:
•	First one is – Sales of a company on the website
•	second one is – Delivery metrics for the online advertising campaigns that the e-commerce website is running

we will assume that we have the following :
feedbacks.csv:  
	-Timestamp: Date and time of the transaction expressed according to the Unix time system
	-Environment: Type of environment on which the transaction took place (web or app)
	-Os: Type of OS on which the transaction took place (Android, Windows, Mac OS, Other, iOS)
    -User ID: Cookie-centric identifier of the user (for each browser or device used there is a different user ID) 
    -Context ID: Here we suppose that a classification system of the website company engine uses to identify users based on their interaction with an advertiser's website. The context is cookie-centric and evolves over time.
        -0	the company doesn't know the visitor (first time he visit the website).
        -1 knows the visitor (he has visited the website before)
        -2	The visitor has seen a non specific product page = homepage only
        -3	The visitor has seen the listing page ( suppose here it is a list of products types)
        -4	The visitor has seen 1 product page
        -5	The visitor has seen 2 or 3 product pages
        -6	The visitor has seen 4 or more product pages
        -7	The visitor has made one purchase (1 or several products bought)
        -8	The visitor has made 2 or 3 purchases (1 or several products bought per purchase)
        -9	The visitor has made 4 or more purchases (1 or several products bought per purchase)
    -


