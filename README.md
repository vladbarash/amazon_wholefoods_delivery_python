

Prerequisites:
- Amazon app on mobile device
- Terminal and some technical knowledge

Step 1: Configure mitmproxy 
* Follow steps in [this tutorial](https://medium.com/testvagrant/intercept-ios-android-network-calls-using-mitmproxy-4d3c94831f62) to intercept network traffic.

Step 2: Make network request to Amazon
* With mitmproxy terminal window open and successfully intercepting network traffic, open Amazon app on your mobile device, add Whole Foods items to cart, and proceed to checkout.

Step 3: Aquire your cookie
* After attempting to checkout, you will likely be met with the `No delivery windows available` screen.
* Within mitmproxy terminal window, navigate to the http request to the `https://www.amazon.com/gp/checkoutportal/enter-checkout`  endpoint.
* Press `e` on your keyboard, press `1` to select curl, enter a path and file name:
![](https://i.imgur.com/4C6mA5A.png)

* Open the txt file you just saved. 
* We need to get the http request to python (or your language of choice) here’s one option:
	* Open Postman, Click Import, Paste Raw Text, paste the curl command, click Import.
	* Click Send to test the http request.
	* Confirm the response contains the string `No delivery windows available`:
![](https://i.imgur.com/5aEh0NO.png)

	* Click Code and generate a python requests code snippet
* Paste into a `.py` file.

Step 4: Operationalize
* See `run.py` file for full code. Replace `[...]` with your own values. The script:
	* Queries Amazon’s servers using your personal cookie, receives a response, checks how many instances of the string `No delivery windows available` is in the response. Since Amazon allows for ordering grocery deliveries for the current day and the next day, we will find the string in the response 2 times if there are absolutely no delivery windows, 1 time if either today or tomorrow contains a delivery windows, and 0 times if there are delivery windows available both today and tomorrow.
	* Sends a text message using Twilio API to your phone number. To operationalize this step you’d need to create an account on Twilio, fund it, and acquire a phone number. You can use your own method for notifications.
	* Spin up an EC2 instance and move the run.py file onto there. To operationalize this step you’d need to have an AWS account. You can use your own method for a compute resource.
	* `crontab -e` to edit your cron jobs. Add `* * * * * python run.py` to run every minute and `:wq` to exit.

Step 5: Monitor
* The script is set up and you can now monitor your texts to jump on a delivery window becoming available.
