# Practice Lab06: Manage Windows Apps

## Summary

In this lab, you create and deploy cloud-based apps using Intune and the Company Portal Website.

### Prerequisites

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 2: Configure and deploy Microsoft 365 Apps from Intune

### Scenario

All the users at Contoso require Microsoft 365 Apps. You've been asked to deploy the 64-bit versions of Microsoft Excel, Outlook, PowerPoint and Word to their Windows devices. You also need to ensure they are configured for the Current Channel for updates.

### Task 1: Verify installed apps on MD102-WS1

1. On **MD102-WS8**, on the taskbar, select **Start** and then select the **Settings** app.

2. In the **Settings** app, select **Apps** and on the **Apps & features** page.

   > Verify that **Microsoft 365 Apps for enterprise - en-us** is not listed.

3. Close all open windows.

### Task 2: Add Microsoft 365 apps to Intune

1. On **MD102-WS1**, in the **Microsoft Intune admin center**, select **Apps**.

2. In the **Apps | Overview** blade, select **All Apps**. In the details pane, select **Add**.

3. In the **Select app type** blade, under **Microsoft 365 Apps**, select **Windows 10 and later** , and then click **Select**.

4. On the **Add Microsoft 365 Apps** blade, configure the following options and select **Next**:

    - Suite Name: **Microsoft 365 Apps for Contoso**

    - Suite Description: **Microsoft 365 Apps** (Select **Edit Description** to enter this information.)

5. On the **Configure app suite** tab, expand the **Select Office apps** dropdown, and ensure that only the following apps are selected:

    - Excel

    - Outlook

    - PowerPoint

    - Word

6. On the **App suite information** section, configure the following options:

     - Architecture: **64-bit**

     - Default file format: **Office Open XML Format**

     - Update channel: **Monthly Enterprise Channel**

7. On the **properties** section, configure the following options and select **Next**:

     - Accept the Microsoft Software License Terms on behalf of users: **Yes**
     
8. On the **Assignments** tab, in the **Required** section, select **Add group.**

9. On the **Select groups** blade, select **Contoso**, and then choose **Select**.

10. Select **Next**. On the **Review + Create** tab, select **Create**.

11. On the **Microsoft 365 Apps for Contoso** page, select **Properties**.

12. In the details pane verify that **Contoso** is listed under **Required** in the **Assignments** section.

### Task 3: Request policy synchronization from the Intune console

1. In the **Microsoft Intune admin center**, select **Devices** and then select **All devices**.

2. In the details pane, select **MD102-WS8**.

3. On the **MD102-WS8** blade, select **Sync** and when prompted select **Yes**.

   > Intune will contact the device and tell it to synchronize all policies. This may take up to 15 minutes. You may choose to Sync from **MD102-WS8**

### Task 4: Verify Microsoft 365 apps are installed

1. Switch to **MD102-WS8** and wait approximately 10-15 minutes for the Microsoft 365 Suite to install on the device.

2. Sign out of **MD102-WS8** and then sign back in as **Megan Bowen** with the PIN **102938**.

3. On **MD102-WS8**, on the taskbar, select **Start** and then select the **Settings** app.

4. In the **Settings** app, select **Apps** and on the **Apps & features** page, scroll down and verify that **Microsoft 365 Apps for enterprise - en-us** is listed.

5. Close the **Settings** app and select the **Start** button.

6. In the app list, scroll down to **W** and select **Word** and verify that the app opens.

7. Close all open windows.

8. Sign out of MD102-WS8.

### Task 5: Monitor app installation status in Intune

1. Switch to **MD102-WS1**.

2. In the **Microsoft Intune admin center**, select **Apps**.

3. On the **Apps | Overview** blade, select **Monitor** and then select **App install status**.

4. In the details pane, select **Microsoft 365 Apps for Contoso**.

5. In the details pane, under **Monitor** and under **User install status**, verify that **1** is displayed under Installed.

   _Note: It may take some time for the information to display._
   
   _Note: This indicates that the app is installed on one device and for one user._

6. Select **Device install status**.

   > In the details pane, you can see the devices that the app is installed on, and also the name of the user. The **Device Name** column should list **MD102-WS8** and the **Status** column should say **Installed**. This means that the app is installed on MD102-WS8.

7. In the **Microsoft Intune admin center**, select **Devices**.

8. On the **Devices | Overview** blade, select **All devices** and then in the details pane, select **MD102-WS8**.

9. On the **MD102-WS8** blade, select **Managed Apps**.

10. On the **MD102-WS8 | Managed Apps** blade, in the details pane, select **Microsoft 365 Apps for Contoso**.

   > On the **Microsoft 365 Apps for Contoso - Installation details** window, you can see the entire lifecycle of the application, that is - when it was created, assigned, installation time and status and the last time the device checked in (synced with Intune).

11. Close all open windows.

**Results**: After completing this exercise, you will have successfully configured and deployed Microsoft 365 Apps from Intune.

**END OF LAB**
