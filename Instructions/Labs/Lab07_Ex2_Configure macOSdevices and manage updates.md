# Practice Lab07: Manage macOS Devices

## Summary

In this lab, you use Microsoft Intune to create a device restriction profile and an update policy for macOS devices.

## Exercise 2: Configure macOS devices and manage updates

### Scenario

Your company has recently deployed Mac devices. These devices need to be configured properly to ensure security and compliance. As part of this task, you are required to create a device restriction profile and an update policy for these Mac OS devices.

### Task 1: Create a device restriction profile

1. Sign in to **SEA-WS3** as **Admin** with the password **Pa55w.rd**. 

1. On the taskbar, select **Microsoft Edge**.

1. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**.

1. Sign in as user `Admin@yourtenant.onmicrosoft.com`, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**.

1. In the Microsoft Intune admin center, in the left navigation pane select **Devices**.

1. On the **Devices | Overview** page, under the **Manage devices** section, select **Configuration**.

1. On the **Devices | Configuration** page, in the **Policies** pane, select **+ Create** and then select **+ New Policy**.

1. In the **Create a profile** tab, select the following options, and then select **Create**:

   - Platform: **macOS**
   - Profile type: **Templates**
   - Template name: **Device restriction**

1. In the **Basics** tab, enter the following information, and then select **Next**:

   - Name: **Contoso default macOS device restriction profile**
   - Description: **Default settings for macOS devices** 

1. On the **Configuration settings** tab, expand **Password**.

1. Select **Yes** next to **Require password** and **Block simple passwords**.

1. Select **Alphanumeric** next to **Require password type**.

1. Enter **6** next to **Minimum password length**.

1. Select **15 minutes** next to **Maximum minutes after screen lock before password is required**

1. Select **5 minutes** next to **Maximum minutes of inactivity until screen locks**.

1. Enter **90** next to **Password expiration (days)**.

1. Enter **5** next to **Prevent reuse of previous passwords**.

1. Select **Next**.

1. On the **Scope tags** tab, select **Next**.

1. On the **Assignments** tab, select **Add all users** and select **Next**.

1. On the **Review + create** tab, select **Create**.

### Task 2: Crate a macOS update profile ### 

1. In the Microsoft Intune admin center, in the left navigation pane select **Devices**.

1. On the **Devices | Overview** page, under the **By platform** section, select **macOS**.

1. On the **macOS | macOS devices** page, under the **Manage updates** section, select **macOS updates** 

1. On the **macOS | macOS updates** page, select **+ Create profile**.

1. In the **Basics** tab, enter the following information, and then select **Next**:

   - Name: **Contoso default macOS update profile**
   - Description: **Default settings for macOS updates**

1. On the **Update policy settings** tab, under **Upadte policy behaviour settings**, select the following settings:

   - Critical updates: **Download only**
   - Firmware updates: **Install immediately**
   - Configuration file updates: **Install immediately**
   - All other updates (OS, built-in apps): **Install immediately**

1. On the **Update policy settings** tab, under **Update policy schedule settings**, select **Update at next check-in** next to **Schedule type** and select **Next**.

1. On the **Scope tags** tab, select **Next**.

1. On the **Assignments** tab, select **Add all users** and select **Next**.

1. On the **Review + create** tab, select **Create**.

**END OF THE LAB**
