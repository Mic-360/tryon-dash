import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { RootState } from './store';

export interface Business {
  _id: string;
  businessName: string;
  businessEmail: string;
  businessCreated_at: string;
  businessAPIKey: string;
  businessPassword: string;
}

interface BusinessState {
  businesses: Business[];
}

const initialState: BusinessState = {
  businesses: []
};

export const businessSlice = createSlice({
  name: 'business',
  initialState,
  reducers: {
    addBusiness: (state, action: PayloadAction<Business>) => {
      state.businesses.push(action.payload);
    },
    setBusinesses: (state, action: PayloadAction<Business[]>) => {
      state.businesses = action.payload;
    }
  }
});

export const { addBusiness, setBusinesses } = businessSlice.actions;

export const selectAllBusinesses = (state: RootState) => state.business.businesses;

export default businessSlice.reducer;