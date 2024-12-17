# Practice Lab05: Manage Windows Updates

## Summary

### Prerequisites

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 1: Creating a Feature Update profile

### Scenario

### Taks 1: Enroll a device

1. Sign in to **MD102-WS9** as **Admin** with the password **Pa55w.rd**.

2. On the **MD102-WS9** taskbar, select **Start** and then select **Settings**.

3. In **Settings**, select **Accounts**.

4. On the Accounts page, select **Access work or school**.

5. In the **Access work or school** page, select **Enroll only in device management**.

6. In the **Microsoft account** window, type **`DiegoS@yourtenant.onmicrosoft.com`** and then select **Next**.

7. On the **Enter password** page, enter your user password provided by your instructor and then select **Sign in**.

8. On the **Stay signed in?** page, select **No**.

9.  On the **Setting up your device** page, select **Got it**. 

10. Close the **Settings** window.

### Task 2: Create a device group with device to update

1. Sign in to **MD102-WS1** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. Select **Groups**, then select **New group**.

6. Type **Windows Update Devices** as the group name.

7. On Members select **No members selected**, then search for the **MD102-WS9** we enrolled in Task 1 and select it.

8. Select **Select** to add the member.

9. Select **Create** to create the group.

### Task 3: Create Feature Update deployment Profile

1. Sign in to **MD102-WS1** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. Select **Devices**, then select **Windows**

6. Select **Windows Updates**, then select **Feature updates**, then select **+Create Profile** to start the creation of a new Feature update deployment profile. 

7. Type **Windows Feature Update Profile** in **Name**.

8. Select the latest Windows Update from the drop down menu for **Feature update to deploy**.

9. Select **Next**.

10. In the next screen select **+Add groups** and select the group **Windows Update Devices**. 

11. Select **Select** to add the group to the assignemnt.

12. Select **Next**.

13. On the page **Review + Create** select **Create** to create the Windows Feature Update Profile.

### Task 4: Verify the assignemnt in the Intune admin center

1. Sign in to **MD102-WS1** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. Select **Devices**, then select **Windows**.

6. Select the device **MD102-WS9**.

7. On the top bar select **Sync** to start a synchronisation cycle for this device, then select **Yes**.

8. On the left side select **Device configuration**.

9. After this short period of time there wont be shown anything. As you can see in the top of the screen it can take time to show any data. But here you would see the Feature Update Profile assigned. 

**`Recently updated information can take up to 20 minutes to be available in this report.`**

**Results**: After completing this exercise, you will have successfully created and assigned a Windows Feature Update Profile. Also you have the knowledge to check the status of the assignment to the device.

**END OF LAB**