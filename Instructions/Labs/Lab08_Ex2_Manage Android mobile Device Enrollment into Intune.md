# Practice Lab08: Manage mobile devices

## Summary

In this lab, you use Microsoft Intune manage device enrollment for iOS/iPadOS and Android devices. 

### Prerequisites

To successfully complete all tasks, a Google account is required. This is essential for setting up a Managed Google Play account, which acts as a bridge between Intune and Android devices. The Managed Google Play account enables secure communication, allowing Intune to deploy apps, enforce policies, and manage updates. Without this integration, Intune cannot effectively manage Android devices. 

The instructions below are only intended to simulate a real-life scenario for training purposes and assume that a valid Apple account already exists. Students are not required to create an Apple account or a certificate in the Apple Push Certificates Portal. If users choose to create an Apple account, they are solely responsible for ensuring that their actions comply with Apple's applicable terms and conditions, including but not limited to the Apple MDM Certificate Agreement. The authors of this guide assume no responsibility for the creation or use of Apple accounts outside of these terms.

## Exercise 2: Manage Android mobile Device Enrollment into Intune

### Scenario

Your organization has recently acquired multiple iOS/iPadOS devices and has chosen to manage them exclusively through Intune. As part of this initiative, you have been assigned the responsibility of setting up the environment for enrollment, ensuring all prerequisites are met, and applying a device name template to all iOS/iPadOS devices.

Additionally, your company has decided to implement a Bring Your Own Device (BYOD) policy, allowing employees to use their personal devices for work purposes. To streamline the enrollment process and ensure data protection, the company has made the decision to enroll all BYOD devices using web based enrollment through Microsoft Intune. 