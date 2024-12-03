# Practice Lab08: Manage mobile devices

## Summary

In this lab, you use Microsoft Intune manage device enrollment for iOS/iPadOS and Android devices.

### Prerequisites

To complete all tasks successfully, an Apple account is necessary. This account is crucial for creating an Apple MDM push certificate. The Apple Push Certificate serves as a digital handshake between Intune and Apple devices, establishing a secure and trusted connection for transmitting commands, policies, and updates. Without this certificate, Intune cannot manage iOS/iPadOS devices. 

The instructions below are only intended to simulate a real-life scenario for training purposes and assume that a valid Apple account already exists. Students are not required to create an Apple account or a certificate in the Apple Push Certificates Portal. If users choose to create an Apple account, they are solely responsible for ensuring that their actions comply with Apple's applicable terms and conditions, including but not limited to the Apple MDM Certificate Agreement. The authors of this guide assume no responsibility for the creation or use of Apple accounts outside of these terms.

## Exercise 1: Manage iOS/iPadOS Device Enrollment into Intune

### Scenario

Your organization has recently acquired multiple iOS/iPadOS devices and has chosen to manage them exclusively through Intune. As part of this initiative, you have been assigned the responsibility of setting up the environment for enrollment, ensuring all prerequisites are met, and applying a device name template to all iOS/iPadOS devices.

Additionally, your company has decided to implement a Bring Your Own Device (BYOD) policy, allowing employees to use their personal devices for work purposes. To streamline the enrollment process and ensure data protection, the company has made the decision to enroll all BYOD devices using web based enrollment through Microsoft Intune. 

### Task 1: Create an Apple push certificate

1. Sign in to **SEA-WS3** as **Admin** with the password **Pa55w.rd**. 

1. On the taskbar, select **Microsoft Edge**.

1. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**.

1. Sign in as user `Admin@yourtenant.onmicrosoft.com`, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**.

1. In the Microsoft Intune admin center, in the left navigation pane select **Devices**.

1. On the **Devices | Overview** page, under the **By platform** section, select **iOS/iPadOS**.

1. On the **iOS/iPadOS | iOS/iPadOS devices** page, under the **Device onboarding** section, select **Enrollment**.

1. On the **iOS/iPadOS | Enrollment** page, select **Apple MDM Push Certificate**.

1. On the **Configure MDM Push Certificate** blade, under step 1, select **I agree.** and then select **Download your CSR** under step 2.

1. On the **Configure MDM Push Certificate** blade, under step 3, select **Create your MDM push Certificate**.

1. On the new tab in Microsoft Edge, sign in with your Apple Account.

1. On the page **https://identity.apple.com/pushcert/**, select **Create a Certificate**.

1. In the Apple Push Certifiactes Portal, read the Terms of Use and select **I have read and agree to these terms and conditions.** and select **Accept**.

1. On the **Create a New Push Certificate** pane, select **Choose File**.

1. In the **Open** box, in the left navigation pane, select **Downloads**, then select **IntuneCSR.csr** and then Select **Open**.

1. On the ** Create a New Push Certificate** pane, select **Upload**.

1. On the **Confirmation** pane, select **Download**.

1. Switch back to the tab **intune.microsoft.com**.

1. On the **Configure MDM Push Certificate** blade, under step 4, enter your Apple ID.

1. On the **Configure MDM Push Certificate** blade, under step 5, under **Apple MDM push certificate**, select **Select a file**.

1. In the **Open** box, in the left navigation pane, select **Downloads**, then select **MDM_Microsoft Corporation_certificate.pem** and select **Open**.

1. On the **Configure MDM Push Certificate** blade, select **Upload**.

### Task 2: Create an enrollment program token

1. In the Microsoft Intune admin center, in the left navigation pane select **Devices**.

1. On the **Devices | Overview** page, under **By platform**, select **iOS/iPadOS**.

1. On the **iOS/iPadOS | iOS/iPadOS devices** page, under the **Device onboarding** section, select **Enrollment**.

1. On the **iOS/iPadOS | Enrollment** page, under **Bulk Enrollment Methods**, select **Enrollment program tokens**.

1. On the **Enrollment program tokens** page, select **+ Add**.

1. On the **Add enrollment program token** page, on the **Basics** tab, select the checkbox **I agree.** to grant permission to Microsoft to send user and device information to Apple, then select **Download your public key** and select **Create a token via Apple Busiess Manager**.

1. On the new tab in Microsoft Edge, finish the steps to create a token in Apple Business Manager.

1. Switch back to the tab **intune.microsoft.com**.

1. On the **Basics** tab, enter your Apple ID next to **Apple ID**.

1. On the **Basics** tab, select **Select a file** next to Apple token.

1. In the **Open** box, in the left navigation pane, select **Downloads**, then select your Appel token a then select **Open** and then select **Next**.

1. On the **Scope tags** tab, select **Next**.

1. On the **Review + create** tab, select **Create**.

### Task 3: Create an Apple enrollment profile

1. In the Microsoft Intune admin center, in the left navigation pane select **Devices**.

1. On the **Devices | Overview** page, under **By platform**, select **iOS/iPadOS**.

1. On the **iOS/iPadOS | iOS/iPadOS devices** page, under the **Device onboarding** section, select **Enrollment**.

1. On the **iOS/iPadOS | Enrollment** page, select **Enrollment program tokens**.

1. On the **Enrollment program tokens** page, select a token.

1. On the tokens page, under **Manage**, select **Profiles**, then select **+ Create profile** and then select **iOS/iPadOS**.

1. On the **Create profile** page, in the **Basics** tab enter the following information and select **Next**:

    - **Name**: Contoso ADE profile for iOS/iPadOS
    - **Description**: This is a standard automated device enrollment profile for all company owned iOS/iPadOS devices.

1. On the **Management Settings** tab, select the following settings and then select **Next**: 

    - User affinity: **Enroll with User Affinity**
    - Authentication Method: **Setup Assistant with modern authentication**
    - Install Compay Portal with VPP: **Don´t use VPP**
    - Supervised: **Yes**
    - Locked enrollment: **Yes**
    - Sync with computers: **Allow All**
    - Await final configuration: **Yes**
    - Apply device name template (supervised only): **Yes**
    - Device Name Template: **Contoso{{DEVICETYPE}}-{{SERIAL}}**
    - Activate cellular data: **No**

1. On the **Setup Assistant** tab, enter the following information:  and then select **Next**.

    - **Department**: Sales
    - **Department Phone**: 0000 (TBD)

1. On the **Setup Assistant** tab, select **Hide** for the switches of the following settings and then select **Next**:

    - Passcode
    - Apple ID
    - Terms and conditions
    - Touch ID and Face ID
    - Apple Pay
    - Zoom
    - Siri
    - Diagnostics Data
    - Display Tone
    - Privacy
    - Home Button
    - iMessage & FaceTime
    - Onboarding
    - Screen Time
    - SIM Setup
    - Software Update
    - Watch Migration
    - Appearance
    - Device To Device Migration

1. On the **Review + create** tab, select **Create**.

### Task 4: Assign an enrollment profile to a device

> To finish tis task, devices must be assigned to the right MDM server in Apple Business Manager.

1. In the Microsoft Intune admin center, in the left navigation pane select **Devices**.

1. On the **Devices | Overview** page, under **By platform**, select **iOS/iPadOS**.

1. On the **iOS/iPadOS | iOS/iPadOS devices** page, under the **Device onboarding** section, select **Enrollment**.

1. On the **iOS/iPadOS | Enrollment** page, under **Bulk Enrollment Methods**, select **Enrollment program tokens**.

1. On the **Enrollment program tokens** page, select your token.

1. On the tokens page, under **Manage**, select **Profiles** and then select the profile **Contoso ADE profile for iOS/iPadOS**.

1. On the **Contoso ADE profile for iOS/iPadOS** page, under **Manage**, select **Assign devices**.

1. On the **Contoso ADE profile for iOS/iPadOS | Assign devices** page select **+ Add Devices**.

1. On the **Add Devices** blade, select a device and then select **Add**.

1. On the **Contoso ADE profile for iOS/iPadOS | Assign devices** page, select **Save**.

### Task 5: Set up just-in-time registration

1. In the Microsoft Intune admin center, in the left navigation pane select **Devices**.

1. On the **Devices | Overview** page, under **Manage devices**, select **Configuration**.

1. On the **Devices | Configuration** page, select **+ Create** section and then select **+ New Policy**.

1. In the **Create a profile** blade, select the following options:

    - Platform: **iOS/iPadOS**
    - Profile type: **Templates**

1. Select **Device features** from the list of templates and then elect **Create**.

1. On the **Basics** tab, enter the following information and then select **Next**:

    - Name: **iOS/iPadOS JIT registration policy**
    - Description: **Configuration of the single sign-on app extension that uses the Apple SSO extension to enable just-in-time registration.**

1. On the **Configuration settings** tab, expand the section **Single sign-on app extension**.

1. Under **All enrollment types**, next to **SSO app extension type**, select **Microsoft Entra ID**.

1. Under **Aditional configuration**, enter the following information:

    - Key: **device_registration**
    - Type: **String**
    - Value: **{{DEVICEREGISTRATION}}**

1. Under **Additional configuration** add a second key-value pair by entering the following information and then select **Next**:

    - Key: **browser_sso_interaction_enabled**
    - Type: **Integer**
    - Value: **1**

1. On the **Scope tags** tab, select **Next**.

1. On the **Assignments** tab, select **Add all users** and then select **Next**.

1. On the **Review + Create** tab, select **Create**.

### Task 6: Create an enrollment profile for BYOD iOS/iPad OS devices.

1. In the Microsoft Intune admin center, in the left navigation pane select **Devices**.

1. On the **Devices | Overview** page, under **By platform**, select **iOS/iPadOS**.

1. On the **iOS/iPadOS | iOS/iPadOS devices** page, under the **Device onboarding** section, select **Enrollment**.

1. On the **iOS/iPadOS | Enrollment** page, under **Enrollment Options**, select **Enrollment types**.

1. On the **Enrollment type profile** page, select **+ Create profile** and then seelct **+ iOS/ iPadOS**.

1. On the **Create enrollment type profile** page, on the **Basics** tab, enter the following information and then select **Next**:

    - Name: **Contoso web based enrollment profile for BYOD iOS/ iPadOS devices**
    - Description: **This profile enables secure and user-friendly web based enrollment of personal iOS/iPadOS devices for Contoso's BYOD program.**

1. On the **Settings** tab, select **Web based device enrollment** next to **Enrollment type** and then select **Next**.

1. On the **Assignments** tab, select **Add all users** and then select **Next**.

1. On the **Review + Create** tab, select **Create**

**END OF THE LAB**