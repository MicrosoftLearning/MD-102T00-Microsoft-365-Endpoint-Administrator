# Practice Lab02: Manage Windows Device Configuration

## Summary

In this lab, you will configure BitLocker disk encryption using Intune.

## Exercise 5: Configuring Disk Encryption Using Intune

### Scenario

It's been determined that all the information on SEA-WS2 should be encrypted. You've been asked to configure full disk encryption on SEA-WS2 and require additional PIN authentication at startup.

### Task 1: Configure device configuration policy in Intune

1. Switch to **SEA-WS1** and if necessary, sign in as **Contoso\\Administrator** with the password **Pa55w.rd**. 

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. In the Microsoft Intune admin center, select **Endpoint security** from the navigation bar.

6. On the **Endpoint security | Overview** page, select **Disk encryption**.

7. On the **Endpoint security | Disk encryption** page, in the details pane, select **Create Policy**.

8. On the **Create a profile** page, select the following options, and then select **Create**:

    -   Platform: **Windows**
    -   Profile: **BitLocker**

9. On the **Basics** page, enter the following information, and then select **Next**:

    -   Name: **Contoso BitLocker**
    -   Description: **Enable BitLocker for all devices**

10. In the **Configurations settings** tab, expand **BitLocker** and then configure the following option:

     - Require Device Encyrption: **Enabled**

11. In the **Configurations settings** tab, scroll down to **Operating System Drives** and then configure the following options, leaving all other options to their defaults:

     - Enforce drive encryption type on operating system drives: **Enabled**
     - Require additional authentication at startup: **Enabled**
     - Configure minimum PIN length for startup: **Enabled**
     - Choose how Bitlocker-protected operating system drives can be recovered: **Enabled**
     - Do not enable Bitlocker until recovery information is stored to AD DS for operating system drives: **True**
     - Omit recovery options from the BitLocker setup wizard: **True**
     - Save Bitlocker recovery info to AD DS for operating system drives: **True**

12. In the **Configurations settings** tab, select **Next**.

13. In the **Scope tags** tab, select **Next**.

14. In the **Assignments** tab, type **Contoso** in the search box and then select **Contoso Developer devices**, and then select **Next**.

16. In the **Review + create** tab, select **Save**.

17. Close all open windows on **SEA-WS1**.

### Task 2: Verify and enable BitLocker settings

1. On **SEA-WS2**, sign in as as Contoso\Administrator with the password of Pa55w.rd.
    
2. On the taskbar, select **Start** and then select the **Settings** app.

3. In the **Settings** app, select **Accounts** and then select **Access work or school**.

4. In the **Access work or school** section, select the **Connected to Contoso MDM** link and then select **Info**. Select **Sync**.

5. Select the **Encryption needed** notification.

   _Note: It may take some time until the notification shows up. Windows Focus Assist may also prevent the notification from appearing. You can check notifications manually._

6. On the **Are you ready to start encryption?** dialog, select the checkbox next to **I don't have any other disk encryption software installed, encrypt all my disks**, and select **Yes**.

7. On the **Choose how to unlock your drive at startup?** page, select **Enter a PIN**

8. On the **Enter a PIN** page, in the **PIN** and **Reenter PIN** boxes, enter **123456**, and then select **Set PIN**.

9. On the **Choose how much of your drive to encrypt** page, select **Encrypt used disk space only** and select **Next**.
   
11. On the **Choose which encryption mode to use** page, ensure that **New encryption mode (best for fixed drives on this device)** is selected, and then select **Next**.
    
12. On the **Are you ready to encrypt this drive** page, select **Continue**. Wait for the encryption to complete.

13. At the **Encryption of C: is complete** message, select **Close**, and then restart **SEA-WS2**.

14. When **SEA-WS2** restarts, type **123456** and press **Enter** to unlock the drive.

### Task 3: Verify BitLocker protection

1. Sign in to **SEA-WS2** as **Contoso\\Administrator** with the password **Pa55w.rd**.

2. On the taskbar, select **File Explorer** and then select **This PC**.

3. In the navigation pane, right-click **Local Disk (C:)**, select **Show more options**, and then select **Manage BitLocker**.

4. In the **BitLocker Drive Encryption** window, ensure that you see **C: BitLocker on** status. This means that drive is encrypted. 

5. Close all open windows and sign out of **SEA-WS2**.

**Results**: After completing this exercise, you will have successfully configured disk encryption by using Intune.

**END OF LAB**