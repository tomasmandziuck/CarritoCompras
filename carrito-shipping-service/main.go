package main

import (
	"encoding/json"
	"net/http"
)

type ShippingRequest struct {
	CartTotal float64 `json:"cart_total"`
}

type ShippingOption struct {
	Method string  `json:"method"`
	Cost   float64 `json:"cost"`
}

func getShippingOptions(w http.ResponseWriter, r *http.Request) {
	var request ShippingRequest

	// Decode the incoming JSON request
	err := json.NewDecoder(r.Body).Decode(&request)
	if err != nil {
		http.Error(w, "Invalid request payload", http.StatusBadRequest)
		return
	}

	// Calculate shipping options based on the cart total
	var options []ShippingOption
	if request.CartTotal < 250 {
		options = []ShippingOption{
			{Method: "Standard Shipping", Cost: 5.99},
			{Method: "Express Shipping", Cost: 9.99},
		}
	} else {
		options = []ShippingOption{
			{Method: "Standard Shipping", Cost: 0.0}, // Free for orders > $50
			{Method: "Express Shipping", Cost: 4.99},
		}
	}

	// Respond with the shipping options
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(options)
}

func main() {
	http.HandleFunc("/shipping-options", getShippingOptions)
	http.ListenAndServe(":8080", nil)
}
