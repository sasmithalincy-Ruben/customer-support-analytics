--Tickets by Channel
SELECT
    channel,
    COUNT(*) AS total_tickets
FROM support_tickets
GROUP BY channel
ORDER BY total_tickets DESC;
--Tickets by priority
SELECT
    priority,
    COUNT(*) AS total_tickets
FROM support_tickets
GROUP BY priority
ORDER BY total_tickets DESC;

-- Average first response time by channel
SELECT
    channel,
    ROUND(AVG(first_response_min), 2) AS avg_response_minutes
FROM support_tickets
GROUP BY channel
ORDER BY avg_response_minutes;
--response time by priority
SELECT
    priority,
    ROUND(AVG(first_response_min), 2) AS avg_response_minutes,
    COUNT(*) AS ticket_count
FROM support_tickets
GROUP BY priority
ORDER BY avg_response_minutes DESC;
--average resolution time
SELECT
    priority,
    ROUND(
        AVG(
            (julianday(resolved_at) - julianday(opened_at)) * 24 * 60
        ),
        2
    ) AS avg_resolution_minutes,
    COUNT(resolved_at) AS resolved_tickets
FROM support_tickets
GROUP BY priority
ORDER BY avg_resolution_minutes DESC;
--customer satisfaction by channel
SELECT
    channel,
    ROUND(AVG(csat), 2) AS avg_csat,
    COUNT(csat) AS responses
FROM support_tickets
GROUP BY channel
ORDER BY avg_csat DESC;
-- Ticket resolution rate
SELECT
    COUNT(resolved_at) AS resolved_tickets,
    COUNT(*) AS total_tickets,
    ROUND(
        COUNT(resolved_at) * 100.0 / COUNT(*),
        2
    ) AS resolution_rate_pct
FROM support_tickets;