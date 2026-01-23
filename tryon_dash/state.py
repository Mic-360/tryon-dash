"""State management for TryOn Dashboard."""

import reflex as rx
import httpx
from typing import Any


class Business(rx.Base):
    """Business data model."""
    id: str = ""
    businessName: str = ""
    businessEmail: str = ""
    businessCreated_at: str = ""
    businessAPIKey: str = ""


class Log(rx.Base):
    """Log entry data model."""
    id: str = ""
    personImage: str = ""
    clothImage: str = ""
    clothType: str = ""
    num_inference_steps: int = 0
    seed: int = 0
    guidance_scale: float = 0.0
    resultImage: str = ""
    productId: str = ""
    userId: str = ""
    businessId: str = ""
    created_at: str = ""


class AppState(rx.State):
    """Main application state."""

    # Business state
    businesses: list[dict[str, Any]] = []
    is_loading: bool = False
    error: str = ""

    # Modal state
    is_modal_open: bool = False
    form_name: str = ""
    form_email: str = ""
    form_password: str = ""
    is_submitting: bool = False

    # API key visibility
    visible_keys: list[str] = []

    # Logs state
    logs: list[dict[str, Any]] = []
    logs_loading: bool = False

    # Logs filters
    filter_user_id: str = ""
    filter_business_id: str = ""
    filter_product_id: str = ""
    filter_cloth_type: str = ""
    filter_inference_steps: str = ""
    filter_seed: str = ""
    filter_guidance_scale: str = ""
    filter_date: str = ""

    # Sidebar state
    sidebar_collapsed: bool = False
    mobile_sidebar_open: bool = False

    @rx.var
    def filtered_logs(self) -> list[dict[str, Any]]:
        """Filter logs based on current filter values."""
        result = self.logs
        
        if self.filter_user_id:
            result = [l for l in result if self.filter_user_id.lower() in l.get("userId", "").lower()]
        if self.filter_business_id:
            result = [l for l in result if self.filter_business_id.lower() in l.get("businessId", "").lower()]
        if self.filter_product_id:
            result = [l for l in result if self.filter_product_id.lower() in l.get("productId", "").lower()]
        if self.filter_cloth_type:
            result = [l for l in result if l.get("clothType", "") == self.filter_cloth_type]
        if self.filter_inference_steps:
            try:
                steps = int(self.filter_inference_steps)
                result = [l for l in result if l.get("num_inference_steps") == steps]
            except ValueError:
                pass
        if self.filter_seed:
            try:
                seed = int(self.filter_seed)
                result = [l for l in result if l.get("seed") == seed]
            except ValueError:
                pass
        if self.filter_guidance_scale:
            try:
                scale = float(self.filter_guidance_scale)
                result = [l for l in result if l.get("guidance_scale") == scale]
            except ValueError:
                pass
        
        return list(reversed(result))

    @rx.var
    def unique_cloth_types(self) -> list[str]:
        """Get unique cloth types from logs."""
        types = set()
        for log in self.logs:
            cloth_type = log.get("clothType", "")
            if cloth_type:
                types.add(cloth_type)
        return sorted(list(types))

    def toggle_key_visibility(self, business_id: str):
        """Toggle API key visibility for a business."""
        if business_id in self.visible_keys:
            self.visible_keys = [k for k in self.visible_keys if k != business_id]
        else:
            self.visible_keys = self.visible_keys + [business_id]

    def is_key_visible(self, business_id: str) -> bool:
        """Check if API key is visible for a business."""
        return business_id in self.visible_keys

    def open_modal(self):
        """Open the add business modal."""
        self.is_modal_open = True
        self.form_name = ""
        self.form_email = ""
        self.form_password = ""
        self.error = ""

    def close_modal(self):
        """Close the add business modal."""
        self.is_modal_open = False

    def set_form_name(self, value: str):
        """Update form name."""
        self.form_name = value

    def set_form_email(self, value: str):
        """Update form email."""
        self.form_email = value

    def set_form_password(self, value: str):
        """Update form password."""
        self.form_password = value

    # Filter setters
    def set_filter_user_id(self, value: str):
        self.filter_user_id = value

    def set_filter_business_id(self, value: str):
        self.filter_business_id = value

    def set_filter_product_id(self, value: str):
        self.filter_product_id = value

    def set_filter_cloth_type(self, value: str):
        # Convert '__all__' back to empty string for filtering
        self.filter_cloth_type = "" if value == "__all__" else value

    def set_filter_inference_steps(self, value: str):
        self.filter_inference_steps = value

    def set_filter_seed(self, value: str):
        self.filter_seed = value

    def set_filter_guidance_scale(self, value: str):
        self.filter_guidance_scale = value

    def set_filter_date(self, value: str):
        self.filter_date = value

    def toggle_sidebar(self):
        """Toggle sidebar collapsed state."""
        self.sidebar_collapsed = not self.sidebar_collapsed

    def toggle_mobile_sidebar(self):
        """Toggle mobile sidebar visibility."""
        self.mobile_sidebar_open = not self.mobile_sidebar_open

    def close_mobile_sidebar(self):
        """Close mobile sidebar."""
        self.mobile_sidebar_open = False

    async def fetch_businesses(self):
        """Fetch all businesses from API."""
        self.is_loading = True
        self.error = ""
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "https://twinverses.in/api/v1/internal/getAllBusinesses",
                    timeout=30.0
                )
                if response.status_code == 200:
                    self.businesses = response.json()
                else:
                    self.error = f"Failed to fetch businesses: {response.status_code}"
        except Exception as e:
            self.error = f"Error fetching businesses: {str(e)}"
        finally:
            self.is_loading = False

    async def create_business(self):
        """Create a new business."""
        if not self.form_name or not self.form_email or not self.form_password:
            self.error = "Please fill in all fields"
            return

        self.is_submitting = True
        self.error = ""

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://twinverses.in/api/v1/internal/createBusiness",
                    json={
                        "businessName": self.form_name,
                        "businessEmail": self.form_email,
                        "businessPassword": self.form_password,
                    },
                    timeout=30.0
                )
                if response.status_code == 200:
                    new_business = response.json()
                    self.businesses = self.businesses + [new_business]
                    self.close_modal()
                    yield rx.toast.success(f"Business created! API Key: {new_business.get('businessAPIKey', 'N/A')}")
                else:
                    self.error = f"Failed to create business: {response.status_code}"
        except Exception as e:
            self.error = f"Error creating business: {str(e)}"
        finally:
            self.is_submitting = False

    async def fetch_logs(self):
        """Fetch all logs from API."""
        self.logs_loading = True
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "https://twinverses.in/api/v1/internal/getAllLogs",
                    timeout=30.0
                )
                if response.status_code == 200:
                    self.logs = response.json()
        except Exception as e:
            print(f"Error fetching logs: {e}")
        finally:
            self.logs_loading = False
