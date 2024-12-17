# Practice Lab08: Manage mobile devices

## Summary

In this lab, you will use Microsoft Intune to configure, deploy, and manage mobile devices and applications for iOS/iPadOS and Android devices.

### Prerequisites

To successfully complete all tasks, a Google account is required. This is necessary for setting up a Managed Google Play account, which acts as a bridge between Intune and Android devices. The Managed Google Play account enables Intune to securely deploy apps, enforce policies, and manage updates. Without this integration, Intune cannot fully manage Android devices.

The instructions provided are intended to simulate a real-world scenario for training purposes and assume that a valid Google account already exists. Students are not required to create a Google account or set up a Managed Google Play account. If users choose to create an account, they are solely responsible for ensuring compliance with Google's terms and conditions. The authors of this guide assume no responsibility for the creation or use of Google accounts outside these terms

## Exercise 2: Manage Android mobile Device Enrollment into Intune

### Scenario

Your organization has recently procured several Android devices for the marketing department to be used exclusively for work purposes and has decided to manage them using Microsoft Intune. As part of this strategy, you have been tasked with configuring the environment for Android enrollment, ensuring all necessary prerequisites are met, and applying a consistent device compliance policy to all corporate-owned devices. This includes setting up a standard profile configuration for work apps and enforcing security policies.

### Task 1: Connect to a Managed google play account

1. Sign in to **MD102-WS1** as **Admin** with the password **Pa55w.rd**. 

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**.

4. Sign in as user `Admin@yourtenant.onmicrosoft.com`, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**.

5. In the Microsoft Intune admin center, in the left navigation pane select **Devices**.

6. In the **Devices | Overview** page, selec **Android**.

7. In the **Android | Android devices** page, under the **Device onboarding** section, select **Enrollment**.

8. On the **Android | Enrollment** page, select **Managed Google Play**.

9.  On the **Managed Google Play** blade, select the checkbox **I agree** under the step 1 to grant Microsoft permission to send both user and device information to Google.

10. Select **Launch Google to connect now.** .

11. On the new Microsoft Edge Window, under **Create Admin Account**  enter the following UPN `Admin@yourtenant.onmicrosoft.com` and select **Next**.

12. On the **Sign up the easy way** page, select **Sign in with Microsoft**.

13. On the ** Permissions requested** page, select **Accept**.

14. On the **Tell us about you** page, in the **Company name**, enter your company name and select **Next**.

15. On the **Add subscriptions to your admin acount** page, select **Next**.

16. On the **Create account** page, select **Agree and continue**.

17. On the **Manage your Android Enterprise devices using Microsoft Intune?** page, select **Allow and create account**.

### Task 2:  Create an enrollment profile for corporate-owned, fully managed user devices

1. In the Microsoft Intune admin center, in the left navigation pane select **Devices**.

2. In the **Android | Android devices** page, under the **Device onboarding** section, select **Enrollment**.

3. On the **Android | Enrollment** page, under **Enrollment Profiles**, select **Corporate-owned, fully managed user deices**.

4. On the **Coorporate-owned, fully managed user devices** page, select **+ Create policy**.

5. In the **Basics** tab, enter the following information and select **Next**:

    - Name: **Default Contoso Fully Managed Enrollment Profile**
    - Description: **The Default Contoso Fully Managed Enrollment Profile ensures corporate-owned Android devices are fully secured, compliant, and preconfigured with required settings and apps.**
    - Toke type: **Corporaet-owned, fully managed (default)**

6. In the **Scope tags** tab, select **Next**.

7. In the **Review + create** tab, select **Create**.

### Task 3: Create a dynamic group

1. In the Microsoft Intune admin center, in the left navigation pane select **Groups**.

2. On the **Groups | Overview** page, select **New group**.

3. On the **New Group** page, enter the following information and select **Add dynamic query**:

    - Group type: **Security**
    - Group name: **Prod_Intune_Android Fully Managed User Devices_Marketing**
    - Description: **Dynamic group for fully managed Android devices in the Marketing department, used in production.**
    - Microsoft Entra roles can be assigned to the group: **No**
    - Membership type: **Dynamic Device**

4. On the **Dynamic membership rules** page, under **Cofigure Rules**, enter the following information and then select **Save**:

    - Property: **enrollmentProfileName**
    - Operator: **Equals**
    - Value: **Default Contoso Fully Managed Enrollment Profile**.

5. On the **New Group** page, select **Create**.

**END OF THE LAB**