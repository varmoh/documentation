## Client-to-DMR Communication

This is about how external clients (like apps or services) talk to the DMR (Distributed Message Relay) system securely and correctly.

### Implement mTLS Authentication for Clients

Clients must prove their identity using mutual TLS (mTLS). This means that when a client connects, both the client and the DMR verify each other’s certificates to ensure trusted communication.

### Design Metadata Schema (Headers/Properties) for Routing

Messages sent by clients include metadata—extra info in message headers or properties—that tells the DMR how to handle or route the message. For example, this includes information about who the message is for, its type, or priority.

### ~~Access Control Policy (Who Can Send to Whom)~~

~~Define and enforce rules that control which clients can send messages to which destinations. This ensures that only authorized communication flows, protecting the system from misuse or attacks.~~

~~Basically, this part ensures clients connect securely, follow the rules, and communicate properly with the DMR.~~
