# **FileMatch API Documentation**

Welcome to the **FileMatch API**! This service allows you to verify if a file's MIME type matches its extension, helping to ensure the integrity of the files in your applications.

[Access Here to Test](https://filematch.vercel.app/docs)

---

## **About**

The **FileMatch API** provides a simple and efficient way to validate file types without saving them to your server. It is designed to help you maintain data integrity and prevent errors in your file-handling workflows.

---

## **How to Use**

To use the API, send a **POST** request to the following endpoint:

```
POST /api/v1/verify/validate-file/
```

### **Headers:**

- `Content-Type`: `multipart/form-data`

### **Body:**

- `file`: The file you wish to validate (required).

---

## **Supported File Extensions**

The following MIME types and their corresponding extensions are supported:

| **MIME Type**                                                   | **Supported Extensions**   |
|-----------------------------------------------------------------|----------------------------|
| `image/jpeg`                                                    | `.jpg, .jpeg`               |
| `image/png`                                                     | `.png`                      |
| `image/gif`                                                     | `.gif`                      |
| `image/bmp`                                                     | `.bmp`                      |
| `image/webp`                                                    | `.webp`                     |
| `image/svg+xml`                                                 | `.svg`                      |
| `image/tiff`                                                    | `.tif, .tiff`               |
| `image/heif`                                                    | `.heif, .heic`              |
| `image/x-icon`                                                  | `.ico`                      |
| `application/pdf`                                               | `.pdf`                      |
| `text/plain`                                                    | `.txt`                      |
| `text/html`                                                     | `.html, .htm`               |
| `text/css`                                                      | `.css`                      |
| `text/javascript`                                               | `.js`                       |
| `application/json`                                              | `.json`                     |
| `application/xml`                                               | `.xml`                      |
| `application/zip`                                               | `.zip`                      |
| `application/x-rar-compressed`                                  | `.rar`                      |
| `audio/mpeg`                                                    | `.mp3`                      |
| `audio/wav`                                                     | `.wav`                      |
| `audio/ogg`                                                     | `.ogg`                      |
| `video/mp4`                                                     | `.mp4`                      |
| `video/x-msvideo`                                               | `.avi`                      |
| `application/vnd.ms-excel`                                      | `.xls, .xlsx`               |
| `application/vnd.openxmlformats-officedocument.wordprocessingml.document` | `.docx`               |
| `application/vnd.ms-powerpoint`                                 | `.ppt, .pptx`               |

---

## **Example Request**

Here is an example of how to send a request to the API using `curl`:

```bash
curl -X POST "https://filematch.vercel.app/api/v1/verify/validate-file/" \
-F "file=@example.jpg"
```

---

## **Example Response**

A successful response will look like this:

```json
{
  "status": "success",
  "message": "The file 'example.jpg' is valid."
}
```

---

## **Support**

If you have any questions or need further assistance, please don't hesitate to contact our support team.

---

© 2024 **FileMatch API** | Built for developers.
