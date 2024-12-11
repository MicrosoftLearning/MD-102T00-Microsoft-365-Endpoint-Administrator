# Practice Lab05: Manage Windows Updates

## Summary

### Prerequisites

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 1: Creating a Feature Update profile

### Scenario

### Task 1: Create a device group with device to update

1. Sign in to **SEA-WS1** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. Select **Groups**, then select **New group**.

6. Type **Windows Update Devices** as the group name.

7. Select **Create** to create the group.

### Task 2: Create Feature Update deployment Profile

1. Sign in to **SEA-WS1** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. Select **Devices**, then select **Windows**

6. Select **Windows Updates**, then select **Feature updates**, then select **+Create Profile** to start the creation of a new Feature update deployment profile. 

7. Type **Windows Feature Update Profile** in **Name**.

8. Select the latest Windows Update from the drop down menu for **Feature update to deploy**.

9. Select **Next**.

10. In the next screen select **+Add groups** and select the group you created in Task 1. 

11. Select **Select** to add the group to the assignemnt.

12. Select **Next**.

13. On the page **Review + Create** select **Create** to create the Windows Feature Update Profile.

### Taks 3: Review the creation and verify the assignemnt in the report

1. Sign in to **SEA-WS1** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. Select **Reports**, then select **Windows updates**.

6. On the top select **Reports**, then select **Windows Feature Update Report**

**Results**: After completing this exercise, you will have successfully opend and modifyed a Windows Autopilot deployment profile to use a device name template.

**END OF LAB**