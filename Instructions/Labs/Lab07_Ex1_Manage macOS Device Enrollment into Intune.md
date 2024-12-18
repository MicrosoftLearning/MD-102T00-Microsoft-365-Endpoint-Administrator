# Practice Lab07: Manage macOS Devices

## Summary

In this lab, you use Microsoft Intune to create a device restriction profile and an update policy for macOS devices.

### Prerequisites

To complete all tasks successfully, an Apple account is necessary. This account is crucial for creating an Apple MDM push certificate. The Apple Push Certificate serves as a digital handshake between Intune and Apple devices, establishing a secure and trusted connection for transmitting commands, policies, and updates. Without this certificate, Intune cannot manage macOS devices. 

The instructions below are only intended to simulate a real-life scenario for training purposes and assume that a valid Apple account already exists. Students are not required to create an Apple account or a certificate in the Apple Push Certificates Portal. If users choose to create an Apple account, they are solely responsible for ensuring that their actions comply with Apple's applicable terms and conditions, including but not limited to the Apple MDM Certificate Agreement. The authors of this guide assume no responsibility for the creation or use of Apple accounts outside of these terms.

## Exercise 1: Manage macOS Device Enrollment into Intune

### Scenario

Your organization has recently acquired multiple macOS devices and has chosen to manage them exclusively through Intune. You have been assigned the responsibility of setting up the environment for enrollment and ensuring all prerequisites are met during this process.

### Task 1: Create an Apple push certificate

1. Sign in to **MD102-WS1** as **Admin** with the password **Pa55w.rd**. 

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**.

4. Sign in as user `Admin@yourtenant.onmicrosoft.com`, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**.

5. In the Microsoft Intune admin center, in the left navigation pane select **Devices**.

6. On the **Devices | Overview** page, under the **By platform** section, select **macOS**.

7. On the **macOS | macOS devices** page, under the **Device onboarding** section, select **Enrollment**.

8. On the **macOS | Enrollment** page, select **Apple MDM Push Certificate**.

9.  On the **Configure MDM Push Certificate** blade, under step 1, select **I agree.** and then select **Download your CSR** under step 2.

10. On the **Configure MDM Push Certificate** blade, under step 3, select **Create your MDM push Certificate**.

11. On the new tab in Microsoft Edge, sign in with your Apple Account.

12. On the page **https://identity.apple.com/pushcert/**, select **Create a Certificate**.

13. In the Apple Push Certifiactes Portal, read the Terms of Use and select **I have read and agree to these terms and conditions.** and select **Accept**.

14. On the **Create a New Push Certificate** pane, select **Choose File**.

15. In the **Open** box, in the left navigation pane, select **Downloads**, then select **IntuneCSR.csr** and then Select **Open**.

16. On the ** Create a New Push Certificate** pane, select **Upload**.

17. On the **Confirmation** pane, select **Download**.

18. Switch back to the tab **intune.microsoft.com**.

19. On the **Configure MDM Push Certificate** blade, under step 4, enter your Apple ID.

20. On the **Configure MDM Push Certificate** blade, under step 5, under **Apple MDM push certificate**, select **Select a file**.

21. In the **Open** box, in the left navigation pane, select **Downloads**, then select **MDM_Microsoft Corporation_certificate.pem** and select **Open**.

22. On the **Configure MDM Push Certificate** blade, select **Upload**.

### Task 2: Create an enrollment program token

1. In the Microsoft Intune admin center, in the left navigation pane select **Devices**.

2. On the **Devices | Overview** page, under **By platform**, select **macOS**.

3. On the **macOS | macOS devices** page, under the **Device onboarding** section, select **Enrollment**.

4. On the **macOS | Enrollment** page, under **Bulk Enrollment Methods**, select **Enrollment program tokens**.

5. On the **Enrollment program tokens** page, select **+ Add**.

6. On the **Add enrollment program token** page, on the **Basics** tab, select the checkbox **I agree.** to grant permission to Microsoft to send user and device information to Apple, then select **Download your public key** and select **Create a token via Apple Busiess Manager**.

7. On the new tab in Microsoft Edge, finish the steps to create a token in Apple Business Manager.

8. Switch back to the tab **intune.microsoft.com**.

9.  On the **Basics** tab, enter your Apple ID next to **Apple ID**.

10. On the **Basics** tab, select **Select a file** next to Apple token.

11. In the **Open** box, in the left navigation pane, select **Downloads**, then select your Appel token a then select **Open** and then select **Next**.

12. On the **Scope tags** tab, select **Next**.

13. On the **Review + create** tab, select **Create**.

### Task 3: Create an Apple enrollment profile

1. In the Microsoft Intune admin center, in the left navigation pane select **Devices**.

2. On the **Devices | Overview** page, under **By platform**, select **macOS**.

3. On the **macOS | macOS devices** page, under the **Device onboarding** section, select **Enrollment**.

4. On the **macOS | Enrollment** page, select **Enrollment program tokens**.

5. On the **Enrollment program tokens** page, select a token.

6. On the tokens page, under **Manage**, select **Profiles**, then select **+ Create profile** and then select **macOS**.

7. On the **Create profile** page, in the **Basics** tab enter the following information and select **Next**:

    - **Name**: Contoso ADE profile for macOS
    - **Description**: This is a standard automated device enrollment profile for all company owned macOS devices.

8. On the **Management Settings** tab, select the following settings and then select **Next**: 

    - User affinity: **Enroll with User Affinity**
    - Authentication Method: **Setup Assistant with modern authentication**
    - Await final configuration: **Yes**
    - Locked enrollment: **Yes**

9.  On the **Setup Assistant** tab, leave all switches on **Show** and enter the following information and then select **Next**.

    - **Department**: Sales
    - **Department Phone**: 0000 (TBD)

10. On the **Account Settings** tab, select **No** next to **Create a local primary account** and select **Next**.

11. On the **Review + create** tab, select **Create**.

### Task 4: Assign an enrollment profile to a device

> To finish tis task, devices must be assigned to the right MDM server in Apple Business Manager.

1. In the Microsoft Intune admin center, in the left navigation pane select **Devices**.

2. On the **Devices | Overview** page, under **By platform**, select **macOS**.

3. On the **macOS | macOS devices** page, under the **Device onboarding** section, select **Enrollment**.

4. On the **macOS | Enrollment** page, under **Bulk Enrollment Methods**, select **Enrollment program tokens**.

5. On the **Enrollment program tokens** page, select your token.

6. On the tokens page, under **Manage**, select **Profiles** and then select the profile **Contoso ADE profile for macOS**.

7. On the **Contoso ADE profile for macOS** page, under **Manage**, select **Assign devices**.

8. On the **Contoso ADE profile for macOS | Assign devices** page select **+ Add Devices**.

9.  On the **Add Devices** blade, select a device and then select **Add**.

10. On the **Contoso ADE profile for macOS | Assign devices** page, select **Save**.

**Results**: After completing this exercise, you will have successfully configured device enrollment for MacOS devices.

**END OF THE LAB**
