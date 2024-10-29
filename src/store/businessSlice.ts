import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { RootState } from './store';

interface Business {
  id: string;
  name: string;
  email: string;
  apiKey: string;
  date: string;
}

interface BusinessState {
  businesses: Business[];
}

const initialState: BusinessState = {
  businesses: [],
};

export const businessSlice = createSlice({
  name: 'business',
  initialState,
  reducers: {
    addBusiness: (state, action: PayloadAction<Business>) => {
      state.businesses.push(action.payload);
    },
  },
});

export const { addBusiness } = businessSlice.actions;

export const selectAllBusinesses = (state: RootState) =>
  state.business.businesses;

export default businessSlice.reducer;
