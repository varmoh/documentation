# Messaging Backbone with RabbitMQ

## Provision RabbitMQ Clusters or Nodes (Locally or via Cloud)

This means setting up RabbitMQ servers that will handle message passing. You can run these servers locally or use cloud services. Clusters involve multiple RabbitMQ nodes working together for reliability and scalability.

## Define Exchanges, Queues, and Routing Rules

RabbitMQ uses exchanges to receive messages and queues to store them before delivery. Routing rules determine how messages move from exchanges to queues based on attributes like routing keys or headers. You have to design this structure to match your message flow and routing needs.

## Enforce Secure Communication (AMQPS with mTLS)

Messages sent between clients and RabbitMQ, or between RabbitMQ nodes, should be encrypted and authenticated using AMQPS (AMQP protocol over TLS). Mutual TLS (mTLS) means both sender and receiver verify each other's identity with certificates, ensuring secure, trusted connections.

## Set Up Message TTLs, DLQs, and Audit Queues

- **Message TTL (Time-To-Live):** Messages expire after a set time if not consumed, preventing old or stuck messages from clogging the system.
- **Dead Letter Queues (DLQs):** Messages that can't be delivered or processed are sent here for inspection or retry.
- **Audit Queues:** Special queues that keep track of message flow or security events for monitoring and troubleshooting. (Might use RabitMQ own interface for that and/or push info to Centops)
