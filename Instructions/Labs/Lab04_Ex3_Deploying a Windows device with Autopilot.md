# Practice Lab04: Manage Windows Autopilot

## Summary

### Prerequisites

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 3: Deploying a Windows device with Autopilot

### Scenario

### Task 1: Create group in Entra ID

1. Sign in to **SEA-WS1** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. From the navigation pane select **Groups**, then select **New group** to start the creation of a group.

6. Enter the name **Autopilot devices** in the section **Group name**.

7. For now we do not need to a members into the group. So select **Create** to create the group. 

8. No in the group overview make sure the group was created successfully. This you can check in the top right corner by selecting the **Bell symbol** to see the notifications .

### Task 2: Generate a device-specific comma-separated value (CSV) file

1. Sign in to **SEA-WS7** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Start**.

3. In the start menu, select the **Searchbar** in the top and search for **Powershell**.

4. You now will see **Windows PowerShell** will be shown as the **Best match** section. 

5. On the right side, select **Run as Administrator**.

6. Notify the User Account Control request, select **Yes** to open the PowerShell as Administrator.

7. To generate the needed .csv file you need to type the following lines in the PowerShell.
Hit enter after every line.

```Powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
```

```Powershell
New-Item -Type Directory -Path "C:\HWID"
```

```Powershell
Set-Location -Path "C:\HWID"
```

```Powershell
$env:Path += ";C:\Program Files\WindowsPowerShell\Scripts"
```
8. After entering this command you need to approve the change of the Execution Policy. You do this by typing **y** in the PowerShell and hit enter.

```Powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

9. After you start to install the needed script you need to approve the installation and import of the NuGet provider. You do this by typing **y** in the PowerShell and hit enter. 

```Powershell
Install-Script -Name Get-WindowsAutopilotInfo
```
10. When you now see a warning for a **Untrusted repository** you need to approve this as well. You do this by typing **y** in the PowerShell and hit enter. 

```Powershell
Get-WindowsAutopilotInfo -OutputFile "C:\HWID\AutopilotHWID.csv"
```

11. Now you have created a .csv file to import this device into Intune to get used in a Autopilot Profile. 

### Task 3: Work with a Windows Autopilot deployment profile

1. Sign in to **SEA-WS7** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. From the navigation pane select **Devices**, then select **Enrollment** in the section **Device onboarding**.

6. On the right side scroll down until you are able to see the section **Windows Autopilot**, select **Devices** in that section.

7. In the **Windows Autopilot devices** overview select **Import** to start the import process.

8. On the right side the dialog **Add Autopilot devices** opens.

9. In this dialog, select the explorer symbol to open the explorer.

10. In the explorer navigate to C:\HWID and select your created **AutopilotHWID.csv** file and select **Open**.

11. There should not be a green checkmark visible, now select **Import**.

12. This process will take some time. You can see the result in the notification area, accessible via the bell symbol in the top of the page. 

13. When the import was successfully you can refresh the view by selecting the **Refresh** button in the **Windows Autopilot devices** area. 

14. Now you see your virtual machine shown with the serial number. Select the **Serial number** to show more information. Notice that no profile is assigned yet. Copy or note down the serial number for later use.

15. Select **Devices | Enrollment** to navigate back to the overview.

16. On the right side scroll down until you are able to see the section **Windows Autopilot**, select **Deployment profiles** in that section.

17. Select the previously created deployment profile **Contoso autopilot profile**.

18. In the navigation area, select **Properties**, then select **Edit** right next to **Assignments** to edit the assignemnts and add a group.

19. In the section for **Included groups**, select **Add groups**.

20. Type **Autopilot devices** in the search bar on the right side. 

21. Select the found group, then select **Select** on the bottom to add the group to the assignment.

22. Now select **Review + save** and then select **Save** to save your changes. 

23. Select **Groups** in the navigation on the left side.

24. Type **Autopilot devives** in the searchbar to find you group.

25. Select your group, then select **Members**, then select **Add members**

26. Type or paste the serial number of your imported virtual machine to search for it. Select the virtual machine and then select **Select** to add it to the group.

27. This will now cause the deployment profile to be assigned to this device. This will take some time. We will check the status later.

28. Close all Windows.

### Task 4: Reset the PC

1. Sign in to **SEA-WS7** as **Admin** with the password **Pa55w.rd**.

2. Open the Start menu and select **Settings**

3. In the searchbar, type **reset**, then select the first result **Reset this PC**.

4. Select **Reset PC** to start the reset.

5. Select **Remove everything**, then select **Local reinstall** and then select **Next**.

6. Wait a few seconds, then select **Reset**.

7. This will take a while.

8. The device will reboot. When the reboot is done login with the user **`JoniS@M365x35851949.OnMicrosoft.com`** and the default user password. 

9. Setup Windows Hello and MFA after the login in OOBE.

10. On the desktop, select the **Start Menu**, then select **Settings**.

11. On the left side select **Accounts**, then select **Access Work or School**.

12. Select the **Connected by JoniS** tab, then select **Info**.

13. Here you can see that the device is now managed by the company and is enrolled into Intune.

### Task 5: Verify Autopilot deployment in Intune admin center

1. Sign in to **SEA-WS1** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. From the navigation pane select **Devices**, then select **Windows**.

6. Select the device you enrolled in Task 4, then select 

7. Select **Hardware**, on the right side you see **Enrollment profile**. Here you can see that this device was enrolled with the profile you created earlier. 

**Results**: After completing this exercise, you will have successfully created a autopilot .csv file, uploaded it and resettet a device to run thought the Autopilot process. 

**END OF LAB**