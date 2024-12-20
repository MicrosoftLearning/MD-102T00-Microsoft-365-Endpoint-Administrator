# Practice Lab02: Manage Windows Device Configuration

## Summary

In this lab, you will configure BitLocker disk encryption using Intune.

### Prerequisites

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 5: Configuring Disk Encryption Using Intune

### Scenario

It's been determined that all the information on MD102-WS3 should be encrypted. You've been asked to configure full disk encryption on MD102-WS3 and require additional PIN authentication at startup.

### Task 1: Configure device configuration policy in Intune

1. Switch to **MD102-WS1** and if necessary, sign in as **Contoso\\Administrator** with the password **Pa55w.rd**. 

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

17. Close all open windows on **MD102-WS1**.

### Task 2: Disable Windows Automatic Enrollment into Microsoft Intune

1. In the Microsoft Intune admin center, select **Devices**.

2. On the Devices pane, under the **Device onboarding** section, select **Enrollment**.

3. In the Enroll devices pane, ensure **Windows** is selected.

4. In the **Enrollment options** section, select **Automatic Enrollment**.

5. On the **MDM user scope** row, make sure **None** is selected and if required, select **Save**.

   _**Note**: By performing this step, you disabled automatic enrollment into Intune for any User that performs an Entra join or Entra registration from a Windows device._

### Task 3: Perform Entra Join and sign in to MD102-WS3 as Diego Siciliani

1. Switch to **MD102-WS3** and sign in as **Admin** with the password of **Pa55w.rd**.

2. On the taskbar, select **Start** and then select **Settings**.

3. In the **Settings** window, select **Accounts**.

4. On the Accounts page, select **Access work or school**.

5. In the **Access work or school** page, select **Connect**.

6. In the **Microsoft account** window, select **Join this device to Entra ID**.

7. On the **Sign in** page, type **`DiegoS@yourtenant.onmicrosoft.com`** and then select **Next**.

8. On the **Enter password** page, enter the user password provided by your instructor and then select **Sign in**.

9. On the **Make sure this is your organization** dialog box, select **Join**.

10. On the **You're all set!** page, select **Done**.

11. On the **Access work or school** page, verify that **Connected to Contoso's Entra ID** is displayed.

11. Sign out of **MD102-WS3**.

12. Select **Other user**, and sign in as **`DiegoS@yourtenant.onmicrosoft.com`**. Wait for the profile to be created.

13. At the **Use Windows Hello with your account** page, select **OK**.

14. On the **More information required** page, select **Next**.

15. On the **Keep your account secure** page, select **Next**.

16. Select **Next**, scan the QR code and **finish** the Authenticator setup.

17. On the verification page, select **Next** and then select **Done**.

18.  On the **Set up a PIN** page, in the **New PIN** and **Confirm PIN** boxes, type **102938** and then select **OK**.

9.  On the **All set!** page, select **OK**.

### Task 4: Verify and enable BitLocker settings

1. On **MD102-WS3**, select **Start** and then select the **Settings** app.

2. In the **Settings** app, select **Accounts** and then select **Access work or school**.

3. In the **Access work or school** section, select the **Connected to Contoso MDM** link, then select **Info** and then select **Sync**.

4. Select the **Encryption needed** notification.

   _Note: It may take some time until the notification shows up. Windows Focus Assist may also prevent the notification from appearing. You can check notifications manually._

5. On the **Are you ready to start encryption?** dialog, select the checkbox next to **I don't have any other disk encryption software installed, encrypt all my disks**, and select **Yes**.

6. On the **Choose how to unlock your drive at startup?** page, select **Enter a PIN**

7. On the **Enter a PIN** page, in the **PIN** and **Reenter PIN** boxes, enter **123456**, and then select **Set PIN**.

8. On the **Choose how much of your drive to encrypt** page, select **Encrypt used disk space only (faster and best for new PCs and drives)** and select **Next**.
   
9. On the **Choose which encryption mode to use** page, ensure that **New encryption mode (best for fixed drives on this device)** is selected, and then select **Next**.
    
10. On the **Are you ready to encrypt this drive** page, select **Continue**. Wait for the encryption to complete.

11. At the **Encryption of C: is complete** message, select **Close**, and then restart **MD102-WS3**.

12. When **MD102-WS3** restarts, type **123456** and press **Enter** to unlock the drive.

### Task 5: Verify BitLocker protection

1. Sign in to **MD102-WS3** as **Diego Siciliani** with the PIN **102938**.

2. On the taskbar, select **File Explorer** and then select **This PC**.

3. In the navigation pane, right-click **Local Disk (C:)**, and then select **Manage BitLocker**.

4. In the **BitLocker Drive Encryption** window, ensure that you see **C: BitLocker on** status. This means that drive is encrypted. 

5. Close all open windows and sign out of **MD102-WS3**.

**Results**: After completing this exercise, you will have successfully configured disk encryption by using Intune.

**END OF LAB**