# Encrypter Dir v1.0 - README

Welcome to **Kichola Malware v1.0**, a dynamic tool for file encryption and decryption. Below, you will find details about how the application works, how to handle the encryption key, and important considerations.

---

## **Program Description**

**Kichola Malware v1.0** is a command-line program that allows you to:
1. View system information.
2. Encrypt files within a specific directory.
3. Decrypt files that were previously encrypted using an encryption key.

The software is designed to run as an **.exe** file.

---

## **Workflow**

### 1. **Encrypt Files**
The user can encrypt files in a specific directory. During this process:
- The program will go through all the files in the directory and encrypt them.
- **Important**: **The encryption key will be automatically deleted after the encryption is completed**.
- **Make sure to copy the key once it is shown, IT WILL BE DELETED!**.

⚠️ **Caution**: Be sure to specify the correct path to avoid encrypting unintended files or directories. Double-check the path before proceeding!

### 2. **Decrypt Files**
The user can decrypt files in a specific directory. During this process:
- The program will go through all the files in the directory and decrypt them.
- **Important**: **The encryption key will be automatically deleted after the decryption is completed**.
- **Make sure to copy the key once it is shown, IT WILL BE DELETED!**.

**Warning**:
```diff
- Make sure to copy the encryption key before it is deleted!
