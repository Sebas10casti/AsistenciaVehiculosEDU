import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private http = inject(HttpClient);
  private readonly apiUrl = environment.apiUrl;

  getVehicles() {
    return this.http.get<any[]>(`${this.apiUrl}/vehicles`);
  }

  createVehicle(vehicleData: any) {
    return this.http.post<any>(`${this.apiUrl}/vehicles/`, vehicleData);
  }
}
