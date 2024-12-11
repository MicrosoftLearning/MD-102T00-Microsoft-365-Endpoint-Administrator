# Practice Lab02: Manage Windows Device Configuration

## Summary

In this lab, you will use Microsoft Intune to create and apply a Configuration profile for a Windows 11 device.

## Exercise 1: Create and apply a Configuration profile

### Scenario

You need to use Entra and Intune to manage members of the Developers department at Contoso. You have been asked to evaluate the solutions that would enable the users to work effectively and securely on Windows 11 devices. Diego Siciliani has volunteered to help you test and evaluate the solution and provide feedback. He has also given you some initial requirements that must be included and applied to the developer's Windows devices:

- The Gaming section in Settings should not be visible.
- The Privacy section in Settings should be restricted as much as possible.
- The C:\DevProjects folder must be excluded from Windows Defender.
- The process devbuild.exe must be excluded from Windows Defender.
- Most used apps and Recently added apps should not be displayed on the Start menu.


### Task 1: Verify device settings

1. Sign in to **SEA-WS2** as Contoso\Administrator with the password of Pa55w.rd.

2. On the taskbar, select **Start** and then select **Settings**.

3. On the **Settings** navigation list, verify that you can see the **Gaming** setting.

4. Select the **Personalization** setting and then on the Personalization page, select **Start**. Ensure that **Show recently added apps** and **Show most used apps** are both set to **On**.

5. In the **Settings** app, select **Privacy & security**.

6. On the **Privacy & security** page, take note of the options under **Security**, **Windows permissions**, and **App permissions**.

7. On the **Privacy & security** page, select **Windows Security** and then select **Open Windows Security**.

8. On the **Windows Security** page, select **Virus & threat protection**.

9. On the **Virus & threat protection** page, under **Virus & threat protection settings**, select **Manage settings** . 

10. Scroll down to **Exclusions** and select **Add or remove exclusions**. At the User Account Control, select **Yes**.

11. On the **Exclusions** page, verify that no exclusions have been configured.

12. Close the **Windows Security** window.

13. Close the **Settings** window.

### Task 2: Enroll the device

1. On the **SEA-WS2** taskbar, select **Start** and then select **Settings**.

1. Select **Start** and then select **Settings**.

1. In **Settings**, select **Accounts**.

1. On the Accounts page, select **Access work or school**.

1. In the **Access work or school** page, select **Enroll only in device management**.

1. In the **Microsoft account** window, type **`DiegoS@yourtenant.onmicrosoft.com`** and then select **Next**.

1. On the **Enter password** page, enter your user password provided by your instructor and then select **Sign in**.

1. On the **Stay signed in?** page, select **No**.

1. On the **Setting up your device** page, select **Got it**. 

1. Close the **Settings** window.

### Task 3: Create a Configuration profile based on scenario requirements

1. Switch to **SEA-WS1**.

2. On **SEA-WS1**, on the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant Admin password.

5. In the Microsoft Intune admin center, select **Devices** from the navigation bar.

6. On the **Devices | Overview** page, select **Configuration**.

7. On the **Devices | Configuration** blade, in the details pane, select **+ Create**, and then select **+ New policy**.

8. In the **Create a profile** blade, select the following options, and then select **Create**:

   - Platform: **Windows 10 and later**
   - Profile type: **Templates**
   - Template name: **Device restrictions**

9. In the **Basics** tab, enter the following information, and then select **Next**:

- Name: **Contoso Developer - standard**
- Description: **Basic restrictions and configuration for Contoso Developers.**

10. On the **Configurations settings** tab, expand **Control Panel and Settings**. 

11. Select **Block** next to the **Gaming** and **Privacy** options.

12. On the **Device restrictions** tab, expand **Start**. 

13. Scroll down and select **Block** next to **Most used apps**, **Recently added apps** and **Recently opened items in Jump Lists**.

14. On the **Device restrictions** tab, scroll down and expand **Microsoft Defender Antivirus**. 

15. Under **Microsoft Defender Antivirus,** scroll down and expand **Microsoft Defender Antivirus Exclusions**.

16. Under **Microsoft Defender Antivirus Exclusions** in the **Files and folders** box, type the following:

    **C:\\DevProjects**.

17. In the **Processes** box, type the following:
    **DevBuild.exe**. 
18. Select **Next** three times until you reach the **Review + create** blade. Select **Create**.

### Task 4: Create the Contoso Developer device group

1. In the Microsoft Intune admin center, in the navigation pane, select **Groups**.

2. On the **Groups | All groups** blade, select **New group**.

3. On the **New Group** blade, enter the following information:

- Group type: **Security**
- Group name: **Contoso Developer devices**
- Group description: **All Windows devices in Contoso Developer department**
- Membership type: **Assigned**

4. Under **Members**, select **No members selected**. 

5. On the **Add members** blade, in the **Search** box type **SEA-WS2**, then select **SEA-WS2** and then select **Select**.

6. On the **New Group** page, select **Create**. 

7. On the **Groups | All groups** blade, verify that the **Contoso Developer devices** group is displayed.

### Task 5: Create a dynamic Entra ID device group

1. In the Microsoft Intune admin center, in the navigation pane, select **Groups**.

1. On the **Groups | Overview** blade, select **All groups**.

1. On the **Groups | All Groups** blade, on the details pane, select **New group**.

2. On the **Group** blade, provide the following values:

   - Group type: **Security**
   - Group name: **Windows Devices**
   - Membership type: **Dynamic Device**

3. Under the **Dynamic Device Members** section, select **Add dynamic query**. 

4. On the **Dynamic membership rules** blade, in the **Rule syntax** section, select **Edit**. 
    
5. In the **Edit rule syntax** text box, add the following simple membership rule and select **OK**.

```
(device.deviceOSType -contains "Windows")
```

6. On the **Dynamic membership rules** blade, select **Save**.

7. On the **New Group** page, select **Create**.

### Task 6: Assign a Configuration profile to Windows devices

1. In the Microsoft Intune admin center, in the navigation pane, select **Devices**. 

2. On the **Devices | Overview** blade, select **Configuration**.

3. On the **Devices | Configuration** blade, in the details pane, select the **Contoso Developer – standard** profile.

4. On the **Contoso Developer – standard** blade, scroll down to the **Assignments** section, and select **Edit**.

5. On the Assignments page, under **Included groups** select **Add groups**.

6. On the **Select groups to include** blade, in the **Search** box, type **Contoso Developer devices**, then select **Contoso Developer devices** and then select **Select**.

7. Back on the **Device restrictions** blade, select **Review + save**, then select **Save**.

### Task 7: Verify that the Configuration profile is applied

1. Switch to **SEA-WS2**.

1. On **SEA-WS2**, on the taskbar, select **Start** and then select **Settings**.

1. In **Settings**, select **Accounts** and then select **Access work or school**.

1. In the **Access work or school** section, select the **Connected to Contoso MDM** link and then select **Info**.

1. In the **Managed by Contoso** page, scroll down and then under Device sync status, select **Sync**. Wait for the synchronization to complete. 

1. Close the **Settings** app.

   _Note: The sync progress may take up to 15 minutes before the profile is applied to the Windows 11 device. Signing out or restarting the device can accelerate this process.

1. On **SEA-WS2**, select **Start** and then select **Settings**. Verify that the **Gaming** setting has been removed.

1. Select **Privacy & security** and notice that many of the privacy settings are now hidden. 

1. Select the **Personalization** setting and then select **Start**. Verify that **Show recently added apps** and **Show most used apps** are set to **Off**. 

1. In the **Settings** app, select **Privacy and Security**.

1. On the **Privacy & Security** page, select **Windows Security** and then select **Open Windows Security**.

1. On the **Windows Security** page, select **Virus & threat protection**.

1. On the **Virus & threat protection** page, select **Manage settings** under **Virus & threat protection settings**. 

1. Scroll down to **Exclusions** and select **Add or remove exclusions**. Select **Yes** at the User Account Control message.

1. On the **Exclusions** page, verify that **C:\\DevProjects** and **DevBuild.exe** are displayed.

1. Close the **Windows Security** page and then close the **Settings** app.

<!-- 
### Task 6: Verify that the Configuration profile is applied

1. In the Microsoft Intune admin center, from the navigation pane, select **Devices**.

2. In the Devices navigation pane, select **Overview**.

3. Select **All devices**, and in the details pane, select **SEA-WS2**. Information about the device such as name, Primary user, and operating system is displayed.

4. In the SEA-WS2 navigation pane, select **Device configuration** and in the details pane take note of the Device configuration profiles assigned to the device. The **State** column should display **Succeeded**, which means that the profiles were applied successfully to the device.

5. In the details pane, select **Contoso Developer – standard**.

6. On the **Contoso Developer – standard** blade, take note of each setting you configured in the profile.

   > The **State** should display **Succeeded** next to all of them.

7.  In the Microsoft Intune admin center, from the navigation pane, select **Home**.

8.  Close Microsoft Edge.
>

**Results**: After completing this exercise, you will have successfully created and assigned a Configuration profile for a Windows 11 device.


