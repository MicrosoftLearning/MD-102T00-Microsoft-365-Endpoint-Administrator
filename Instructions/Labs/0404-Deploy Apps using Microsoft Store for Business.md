# Practice Lab: Deploy Apps using Microsoft Store for Business

## Summary

In this lab, you will configure and deploy cloud-based apps using Microsoft Store for Business integrated with Microsoft Intune.

### Prerequisites

To following lab(s) must be completed before this lab:

- 0101-Managing Identities in Azure AD

- 0102-Synchronizing Identities by using Azure AD Connect

- 0203-Manage Device Enrollment into Intune

- 0204-Enrolling devices into Intune

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Azure AD.

## Exercise 1: Add a Microsoft Store App to Intune

### Scenario

You have decided to integrate Microsoft Store for Business with Intune. You need to configure the Microsoft Store for Business integration settings and the test out the purchase and adding of the apps to the private Contoso app store. You also need to ensure that only people that you assign a purchasing role to are able to buy Microsoft Store for Business apps.

### Task 1: Configure Microsoft Store for Business settings and integration with Intune

1. On **SEA-SVR1**, if necessary, sign in as **Contoso\\Administrator** with the password **Pa55w.rd** and close **Server Manager**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type `https://www.microsoft.com/en-us/business-store` in the address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant Admin password. 

5. In the menu bar, select **Manage**. The **Overview** page displays.

6. On the **Overview** page, select **Settings**.

7. On the **Shop** page, under **Shopping behavior**, configure the **Make everyone a Basic Purchaser** setting to **Off**. 

8. At the **Stop people from buying** message, select **Don't let people buy**. 

   > This restricts Microsoft Store for business purchases to only users that you have specifically assigned a purchasing role to.

9. Select the **Distribute** page.

10. On the **Distribute** page, take note of the current name for the private store. The current name is the name associated with the tenant.

11. Under Management tools, verify that **Microsoft Intune** Status is set to **Active**. If it is not, under **Action** select **Activate**.

12. In Microsoft Edge, open a new tab and browse to https://endpoint.microsoft.com. The Microsoft Endpoint Manager admin center opens.

13. In the Microsoft Endpoint admin center, in the navigation pane, select **Tenant administration**.

14. In the **Tenant admin** navigation pane, select **Connectors and tokens**.

15. On the **Connectors and tokens** page, select **Microsoft Store for Business**. 

16. If necessary, on the **Microsoft Store for Business** page, select **Enable** and then select **Save**. The status should display as **Active**.

17. At the bottom of the Microsoft Store for Business page, select **Sync**.

### Task 2: Purchasing and Adding apps to the Private Store 

1. In Microsoft Edge, switch to the **Microsoft Store for Business** tab (if there's no tab click on the url link **Open the business store**).

2. In the menu bar, select **Shop for my group**.

3. Scroll down to the **Made by Microsoft** section.

4. In the **Made by Microsoft** section, select **Network Speed Test**.

5. On the **Network Speed Test** page, select **Get the app**.

6. Click on the box next to the **I accept this agreement** and select **Accept**

7. On the **Thanks for your order** page, select **Close**.

8. On the Network Speed Test page, select the ellipse button and then select **Manage**.

9. On the Network Speed Test manage page, select the **Private store availability** tab.

10. On the **Private store availability** tab, under **Choose groups of people who can see this app**, select **Everyone**.

11. Repeat steps 2-10 and select the app named **Fresh Paint**.

12. In the menu bar, select **Contoso**. This is a view of the private store which displays the apps that you have purchased and made available to users.

**Results**: After completing this exercise, you will have successfully integrated Microsoft Store for Business with Intune.

## Exercise 2: Deploy Microsoft Store for Business Apps using Intune

### Scenario

Now that you have integrated Microsoft Store for Business with Intune, you need to verify that you can successfully deploy the apps to devices. You decide to deploy the Network Speed Test app to all devices. Aaron Nicholls has agreed to test out the app to make sure it is deployed successfully.

### Task 1: Synchronize Intune with Microsoft Store for Business

1. In Microsoft Edge, switch to the tab that contains **Microsoft Endpoint Manager admin center**.

2. In the Microsoft Endpoint admin center, in the navigation pane, select **Tenant administration**.

3. In the **Tenant admin** navigation pane, select **Connectors and tokens**.

4. On the **Connectors and tokens** page, select **Microsoft Store for Business**. 

5. At the bottom of the Microsoft Store for Business page, select **Sync**.

### Task 2: Deploy Microsoft Store for Business apps

1. On the **Microsoft Endpoint Manager admin center** pane, select **Apps**.

2. In the **Apps | Overview** blade, select **All Apps**. Notice the Apps that have synced from Microsoft Store for Business.

3. In the app list, select **Network Speed Test (Online)**.

4. On the **Network Speed Test (Online)** pane, select **Properties**.

5. Scroll down to the **Assignments** section and then select **Edit**.

6. On the **Edit application** page, under **Required**, select **Add all devices**.

7. Select **Review + save** and then select **Save**.

### Task 3: Force policy synchronization from the Intune console

1. In the **Microsoft Endpoint Manager admin center**, select **Devices** and then select **All devices**.

2. In the details pane, select **SEA-WS1**. 

3. On the **SEA-WS1** blade, select **Sync** and when prompted select **Yes**. 

   > Intune will contact the device and tell it to synchronize all policies. This may take up to 5 minutes.

### Task 4: Verify the app has installed

1. Switch to **SEA-WS1** and if necessary sign in as Aaron Nicholls with the PIN **102938**. Wait approximately 5 minutes for the app to install on the device.

2. On **SEA-WS1**, on the taskbar, select **Start** and then select the **Settings** app.

3. In the **Settings** app, select the **Apps** tile and on the **Apps & features** page, scroll down and verify that **Network Speed Test** is listed.

4. Close the **Settings** app and select the **Start** button.

5. In the app list, scroll down to **N** and select **Network Speed Test** and verify that the app opens.

6. Sign out of SEA-WS1.

### Task 5: Monitor app installation status in Intune

1. Switch to **SEA-SVR1**.

2. In the **Microsoft Endpoint Manager admin center**, select **Apps** in the navigation menu.

3. On the **Apps | Overview** blade, select **Monitor** and then select **App install status**. In the details pane, select **Network Speed Test (Online)**.

4. In the details pane, under **Device status** and under **User status**, verify that **1** is displayed under Installed. 

   _Note: This indicates that the app is installed on one device and for one user. Note that it may take some time for the information to display._

5. Select **Device install status**. In the details pane, you can see the devices that the app is installed on, and also the name of the user. 

6. In the **Microsoft Endpoint Manager admin center**, select **Devices**.

7. On the **Devices | Overview** blade, select **All devices** and then in the details pane, select **SEA-WS1**.

8. On the **SEA-WS1** blade, select **Managed Apps**.

9. On the **SEA-WS1 | Managed Apps** blade, in the details pane, select **Network Speed Test**.

10. On the **Network Speed Test - Installation details** blade, you can see the entire lifecycle of the application, that is - when it was created, assigned, installation time and status and the last time the device checked in (synced with Intune).

11. Close all open windows.

**Results**: After completing this exercise, you will have successfully deployed a Microsoft Store for Business app to a Windows 11 device using Intune.

**END OF LAB**
