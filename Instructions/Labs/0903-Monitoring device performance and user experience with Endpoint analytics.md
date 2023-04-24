# Practice Lab: Monitoring device performance and user experience with Endpoint analytics

## Summary

In this lab you enable Endpoint analytics to monitor device performance and user experience scores and insights.

### Prerequisites

To following lab(s) must be completed before this lab:

- 0203-Manage Device Enrollment into Intune

- 0204-Enrolling devices into Intune

- 0301-Creating and Deploying Configuration Profiles

  Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Azure AD.

### Scenario

You have been asked to monitor startup performance, application reliability, and user experience how often users restart their devices. To acquire this information you need to enable Endpoint analytics.

### Task 1: Enable Endpoint analytics

1. On **SEA-SVR1**, if necessary, sign in as **Contoso\\Administrator** with the password **Pa55w.rd** and close **Server Manager**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://endpoint.microsoft.com** in the address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant Admin password.

5. On the **Microsoft Endpoint Manager admin center** page, select **Reports**.

6. On the **Reports** blade, under **Analytics**, select **Endpoint analytics**. 

7. On the **Endpoint analytics** page, ensure that **Collect device data from** is set to **All cloud-managed devices**, and then select **Start**.

   > Take note of the message at the top of the Overview page. It may take up to 24 hours for scores and insights to display on the page.

8. Switch to **SEA-WS1** and restart the device.

9. If necessary, enter the BitLocker PIN: **1234**.

10. Sign in as **Aaron Nicholls** with the PIN: **102938**.

11. Switch to **SEA-SVR1**.

12. On the **Microsoft Endpoint Manager admin center** page, select **Devices** and then select **All devices**.

13. Select **SEA-WS1**.

14. On the **SEA-WS1** page, select **Sync** and then select **Yes**.

15. On the **SEA-WS1** page, under **Monitor**, select **User experience**.

16. Review the **Endpoint analytics**, **Startup performance**, and **Application reliability** tabs.

    > There may not be any information reported due to the time delay, however read the details on what will be visible on each tab.

17. On the **Microsoft Endpoint Manager admin center** page, select **Reports**.

18. On the **Reports** blade, under **Analytics**, select **Endpoint analytics**. 

    > Note that the same type of information is available in Endpoint analytics, however this information is based upon all enrolled devices.

19. Browse through the Reports available in the Endpoint analytics page.

20. Close Microsoft Edge.

**Results**: After completing this exercise, you will have successfully enabled Endpoint analytics to monitor device performance and user experience scores and insights.

**END OF LAB**
