import { Component, inject } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-vehicles-list',
  imports: [],
  templateUrl: './vehicles-list.component.html',
})
export class VehiclesListComponent { 
  private apiService = inject(ApiService);

}
