# Practice Lab04: Manage Windows Autopilot

## Summary

### Prerequisites

To following lab(s) must be completed before this lab:

- Lab04: Manage Windows Autopilot - Exercise 1: Create a Autopilot profile

## Exercise 2: Modify a Autopilot Profile to use a device name template

### Scenario

In order to identify the devices, which are enrolled with Autopilot, easier you must establish a function to give them a recognisable name. 
The following are specifications are required:

- The Windows Autopilot deployment profile needs to apply a device name template

### Task 1: Open the created profile from Excercise 1

1. Sign in to **SEA-WS1** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. From the navigation pane select **Devices**, then select **Enrollment**. Make sure you are on the page for the Windows Operating System.

6. On the right side in the section **Windows Autopilot** select **Deployment profiles**.

7. Now select your previously created Deployment Profile

8. Under **Mange** select **Properties** 

9. Here you see all the settings made to the deplyoment profile.

### Task 2: Modify the OOBE Settings

1. Select **Edit** in the section **Out-of-box experience (OOBE)** to modify the settings.

2. Turn on the settings **Apply device name template** by select **Yes** for this setting.

3. As you now see a new section has opend in this section you provide a template for the device name.

4. Type **Contoso-%SERIAL%** in the textbox for **Enter a name**.

5. As you now can see this. There are too many characters for the name template.

6. Delete the **-** behind **Contoso** to make the template fit.

7. Now a green checkmark is visible.

8. Select **Review + Save** to go to the review page.

9. Now select **Save** to save the changes you have made.

**Results**: After completing this exercise, you will have successfully opend and modifyed a Windows Autopilot deployment profile. The profile now use a device name template on the enrolled devices.

**END OF LAB**