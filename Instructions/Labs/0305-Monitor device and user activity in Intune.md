# Practice Lab 0305: Monitor device and user activity in Intune

## Summary

In this lab, you will monitor user Sign-in activity, Audit logs, and device information.

### Prerequisites

To following lab(s) must be completed before this lab:

- 0101-Managing Identities in Entra ID

- 0102-Synchronizing identities by using Entra Connect

- 0203-Manage Device Enrollment into Intune

- 0204-Enrolling devices into Intune

- 0301-Creating and Deploying Configuration Profiles

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

### Scenario

You need to review Aaron Nicholls sign-in activity and general information provided by the Audit logs.  You also need to verify the hardware on SEA-WS1 and confirm the configuration profile assigned to this device is successfully applied.

### Task 1: Monitor user activity

1. On **SEA-SVR1**, on the taskbar, select **Microsoft Edge**.

2. In Microsoft Edge, type **https://intune.microsoft.com** in the address bar, and then press **Enter**.

3. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant Admin password.

4. On the **Microsoft Intune admin center** page, select **Users**.

5. On the **Users|All users** pane, select **Sign-ins logs**.

6. In the Details pane, user sign-ins are listed. Select the first entry where the **User** column displays **Aaron Nicholls**.

7. In the **Details** pane, Aaron Nicholls´sign-in details are displayed.

8. Select each of the main pages, including **Basic info**, **Location**, **Device info**, **Authentication Details**, and **Conditional Access**. Scroll to examine information on each page and then select **X** in the top right hand corner to close out of the **Activity Details** page.

9. In the Users navigation pane, select **Audit logs**.

10. In the details pane, audit information is displayed about administrative changes to users. Examine the information by selecting the various entries.

### Task 2: Monitor device information

1. In the Microsoft Intune admin center, from the navigation pane, select **Devices**.

2. In the Devices navigation pane, select **Overview**.

3. Select **All devices**, and in the details pane, select **SEA-WS1**. Information about the device such as name, Primary user, and operating system is displayed.

4. In the SEA-WS1 navigation pane, select **Hardware** and examine the hardware inventory.

5. In the SEA-WS1 navigation pane, select **Discovered apps** and examine the app inventory.

6. In the SEA-WS1 navigation pane, select **Device configuration** and in the details pane take note of the Device configuration profiles assigned to the device. The **State** column should display **Succeeded**, which means that the profiles were applied successfully to the device.

7. In the details pane, select **Contoso Developer – standard**.

8. On the **Contoso Developer – standard** blade, take note of each setting you configured in the profile.

   > The **State** should display **Succeeded** next to all of them.

9. In the Microsoft Intune admin center, from the navigation pane, select **Home**.

10. Close Microsoft Edge.

**Results**: After completing this exercise, you will have successfully monitored user Sign-in activity, Audit logs, and device information.

**END OF LAB**
