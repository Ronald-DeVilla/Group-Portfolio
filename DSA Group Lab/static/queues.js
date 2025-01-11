document.addEventListener("DOMContentLoaded", () => {
    const enqueueInput = document.getElementById("enqueue-input");
    const enqueueBtn = document.getElementById("enqueue-btn");
    const dequeueBtn = document.getElementById("dequeue-btn");
    const outputDiv = document.getElementById("output");

    const updateQueueOutput = (queue) => {
        outputDiv.textContent = queue.length > 0 ? `Queue: ${queue.join(" -> ")}` : "The queue is empty!";
    };

    enqueueBtn.addEventListener("click", async () => {
        const value = enqueueInput.value.trim();
        if (value) {
            try {
                const response = await fetch("/enqueue", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ value })
                });
                const data = await response.json();
                if (response.ok) {
                    updateQueueOutput(data.queue);
                } else {
                    alert(data.error);
                }
            } catch (error) {
                console.error("Error enqueuing value:", error);
            }
        } else {
        }
        enqueueInput.value = "";
    });

    dequeueBtn.addEventListener("click", async () => {
        try {
            const response = await fetch("/dequeue", {
                method: "POST"
            });
            const data = await response.json();
            if (response.ok) {
                updateQueueOutput(data.queue);
            } else {
            }
        } catch (error) {
            console.error("Error dequeuing value:", error);
        }
    });

    const fetchQueueState = async () => {
        try {
            const response = await fetch("/display");
            const data = await response.json();
            updateQueueOutput(data.queue);
        } catch (error) {
            console.error("Error fetching queue state:", error);
        }
    };

    fetchQueueState();
});
